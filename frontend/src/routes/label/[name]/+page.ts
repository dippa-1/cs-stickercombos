import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const csr = true;

export const load: PageLoad = async ({ params }) => {
  if (!params.name?.length) {
    error(404, 'No labels provided')
  }

  const sticker: {
    name: string,
    iconUrl: string,
    rarity: string,
    letters: string,
  } | null = await fetch(`http://localhost:5000/label/${params.name}`).then(res => res.json()).catch(e => error(500, e));
  console.log('Got labeling sticker', sticker);

  return {
    sticker,
  };
};