<script lang="ts">
	import { Heading, Span } from 'flowbite-svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	console.log({ data });
</script>

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
