<script>
	import '../app.pcss';

	import GitHubButton from '$lib/GitHubButton.svelte';
</script>

<div class="relative">
	<div class="absolute right-2 top-2">
		<GitHubButton />
	</div>
</div>

<div class="mx-auto p-8 text-center md:p-16">
	<slot />
</div>
