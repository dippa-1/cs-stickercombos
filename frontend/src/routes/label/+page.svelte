<script lang="ts">
	import { A, Range, Button, Heading, Input, Label, Span } from "flowbite-svelte";
	import type { PageData } from './$types';
	import { browser } from "$app/environment";

  export let data: PageData;

  let label = '';
	let rotation = 0;

	$: if (rotation != null) {
		rotateImage();
	}

	function rotateImage() {
		if (browser) {
			const image = document.getElementById('sticker-image');
			if (image) {
				image.style.transform = `rotate(${rotation}deg)`;
			}
		}
  }
</script>

<Heading tag="h1">Label these stickers</Heading>
<form action="/label" class="mx-auto mb-32 mt-16 flex space-x-2 md:w-2/3 xl:w-1/3">
	<Input bind:value={label} size="lg" type="text" name="label" placeholder="Enter characters" required />
	<div class="my-4"></div>
	<Button type="submit" size="xl"><div>Finish↩</div></Button>
	<Button href='/label/next' type="button" size="xl">Skip</Button>
</form>


<div class="mx-auto md:w-2/3 xl:w-1/3 mb-16">
	<Label>Rotation: {rotation}</Label>
	<Range bind:value={rotation} id="rot" min=-180 max=180 />
</div>

{#if data.sticker}
	<Heading tag="h2">{data.sticker.name}</Heading>

		<hr class="my-4" />
		<ul class="flex justify-center">
				<a href={data.sticker.iconUrl} class="group" target="_blank">
					<li>
						<img
							id="sticker-image"
							src={data.sticker.iconUrl}
							alt={data.sticker.name}
							class="mx-auto transition-transform duration-0"
						/>
						<Span class="text-sm text-gray-500 transition-all group-hover:text-black"
							>{data.sticker.name}</Span
						>
					</li>
				</a>
		</ul>
{/if}
