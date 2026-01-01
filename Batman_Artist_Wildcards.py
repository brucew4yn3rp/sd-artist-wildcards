import random
import gradio as gr
import modules.scripts as scripts
from modules.processing import process_images, Processed


class Script(scripts.Script):
    def title(self):
        return "Artist Wildcards"

    def ui(self, is_img2img):
        artist_tags = gr.Textbox(
            label="Artist Tags (comma separated)",
            lines=4,
            placeholder="artist1, artist2, artist3"
        )

        min_artists = gr.Slider(
            label="Min Artists",
            minimum=0,
            maximum=50,
            step=1,
            value=1
        )

        max_artists = gr.Slider(
            label="Max Artists",
            minimum=1,
            maximum=50,
            step=1,
            value=3
        )

        random_weights = gr.Checkbox(
            label="Random Weights",
            value=True
        )

        min_weight = gr.Slider(
            label="Min Weight",
            minimum=0.05,
            maximum=5.0,
            step=0.05,
            value=0.05
        )

        max_weight = gr.Slider(
            label="Max Weight",
            minimum=0.05,
            maximum=5.0,
            step=0.05,
            value=1.5
        )

        seed = gr.Number(
            label="Seed (-1 = random)",
            value=-1,
            precision=0
        )

        return [
            artist_tags,
            min_artists,
            max_artists,
            random_weights,
            min_weight,
            max_weight,
            seed,
        ]

    def run(
        self,
        p,
        artist_tags,
        min_artists,
        max_artists,
        random_weights,
        min_weight,
        max_weight,
        seed,
    ):
        artists = [a.strip() for a in artist_tags.split(",") if a.strip()]
        total_artists = len(artists)

        if total_artists == 0:
            proc = process_images(p)
            return Processed(p, proc.images, p.seed, proc.all_prompts, proc.infotexts)

        min_artists = min(min_artists, total_artists)
        max_artists = max(min_artists, min(max_artists, total_artists))

        if seed == -1:
            seed = random.randint(0, 2**32 - 1)

        rng = random.Random(seed)
        num_artists = rng.randint(min_artists, max_artists)
        selected = rng.sample(artists, num_artists)

        if random_weights:
            weights = [round(rng.uniform(min_weight, max_weight), 2) for _ in selected]
            total_weight = sum(weights)

            if total_weight > 2:
                weights = [round(w * 2 / total_weight, 2) for w in weights]

            artist_string = ", ".join(
                f"({artist}:{weight})"
                for artist, weight in zip(selected, weights)
            )
        else:
            artist_string = ", ".join(selected)

        if p.prompt:
            p.prompt = f"{p.prompt}, {artist_string}"
        else:
            p.prompt = artist_string

        proc = process_images(p)
        return Processed(
            p,
            proc.images,
            p.seed,
            all_prompts=proc.all_prompts,
            infotexts=proc.infotexts,
        )
