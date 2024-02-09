<script lang="ts">
	import { Heading } from 'flowbite-svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	console.log({ data });
</script>

<Heading tag="h2">Results for "{data.word}"</Heading>

<hr class="my-4" />

<ul>
	{#each data.res as sticker}
		<li>
			<a href={sticker.iconUrl}>
				<img src={sticker.iconUrl} alt={sticker.name} />
				{sticker.name}
			</a>
		</li>
	{/each}
</ul>
