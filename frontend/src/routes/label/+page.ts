import type { PageLoad } from './$types';

export const csr = true;

export const load: PageLoad = async ({}) => {
  const sticker: {
    name: string,
    iconUrl: string,
    rarity: string,
    letters: string,
  } | null = await fetch(`http://localhost:5000/label/next`).then(res => res.json()).catch(e => null);
  console.log('Got labeling sticker', sticker);

  return {
    sticker,
  };
};