<script>
	import { goto } from '$app/navigation';
	import '../app.pcss';

	import { Input, Button, Heading } from 'flowbite-svelte';

	let word = '';

	const submit = () => {
		goto(`/suggest/${word}`)
	}
</script>

<div class="mx-auto p-8 text-center md:p-16">
	<Heading tag="h1">Suggest stickers for a word</Heading>
	<form
		class="mx-auto mb-32 mt-16 flex space-x-2 md:w-2/3 xl:w-1/3"
		on:submit|preventDefault={submit}
	>
		<Input bind:value={word} size="lg" type="text" name="word" placeholder="Enter word" required />
		<div class="my-4"></div>
		<Button type="submit" size="xl">Convert</Button>
	</form>

	<slot />
</div>
