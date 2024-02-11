import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const sticker: {
    name: string,
    iconUrl: string,
  } | null = await fetch(`http://api.cs-tracker.com:8000/label/next`).then(res => res.json()).catch(e => error(500, e));

  if (sticker) {
    console.log('Redirecting to', sticker.name);
    redirect(301, `/label/${sticker.name}`)
  }

  error(404, 'No stickers to label');
};