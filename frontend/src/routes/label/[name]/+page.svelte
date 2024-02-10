<script lang="ts">
	import { A, Range, Button, Heading, Input, Label, Span } from 'flowbite-svelte';
	import type { PageData } from './$types';
	import { browser } from '$app/environment';

	export let data: PageData;

	let labels = [''];
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

	function addTextField() {
		// only if the last field is not empty
		if (labels[labels.length - 1] !== '') labels = [...labels, ''];
	}
</script>

<Heading tag="h1">Label these stickers</Heading>
<form method="post" class="mx-auto mb-32 mt-16 flex space-x-2 md:w-2/3 xl:w-1/3">
	<div class="flex w-full flex-col space-y-2">
		{#each labels as _, i}
			<Input
				bind:value={labels[i]}
				size="lg"
				type="text"
				name="label"
				placeholder="Enter characters"
				required
				maxLength="30"
			/>
		{/each}
		<Button type="button" on:click={addTextField} size="lg">Add text field</Button>
	</div>
	<div class="flex space-x-2">
		<div>
			<Button type="submit" size="lg"><div>Save↩</div></Button>
		</div>
		<div>
			<Button href="/label" type="button" size="lg">Skip</Button>
		</div>
	</div>
</form>

<!-- <div class="mx-auto mb-16 md:w-2/3 xl:w-1/3">
	<Label>Rotation: {rotation}</Label>
	<Range bind:value={rotation} id="rot" min="-180" max="180" />
</div> -->

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
