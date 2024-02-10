<script lang="ts">
	import { Input, Button, Heading, Span } from 'flowbite-svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	console.log({ data });

	let word = '';
</script>

<Heading tag="h1">Suggest stickers to build a word</Heading>
<form action="/suggest" class="mx-auto mb-32 mt-16 flex space-x-2 md:w-2/3 xl:w-1/3">
	<Input bind:value={word} size="lg" type="text" name="word" placeholder="Enter word" required />
	<div class="my-4"></div>
	<Button type="submit" size="xl">Suggest</Button>
</form>

{#if !!data.word?.length && data.res}
	<Heading tag="h2">Results for "{data.word}"</Heading>

	{#each data.res as result}
		<hr class="my-4" />
		<ul class="flex justify-center">
			{#each result as sticker}
				<a href={sticker.iconUrl} class="group" target="_blank">
					<li>
						<img
							src={sticker.iconUrl}
							alt={sticker.name}
							class="mx-auto transition-transform duration-300 group-hover:scale-125"
						/>
						<Span class="text-sm text-gray-500 transition-all group-hover:text-black"
							>{sticker.name}</Span
						>
					</li>
				</a>
			{/each}
		</ul>
	{/each}
{/if}
