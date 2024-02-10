import { error, redirect } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({}) => {
  const sticker: {
    name: string,
    iconUrl: string,
  } | null = await fetch(`http://localhost:5000/label/next`).then(res => res.json()).catch(e => error(500, e));

  if (sticker) {
    console.log('Redirecting to', sticker.name);
    redirect(301, `/label/${sticker.name}`)
  }

  error(404, 'No stickers to label');
};