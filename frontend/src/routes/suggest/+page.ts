import type { PageLoad } from './$types';

export const load: PageLoad = async ({ url }) => {
  const word = url.searchParams.get('word')?.toLowerCase();
  if (!word?.length) {
    console.error('no word provided');
    return {}
  }

  const stickers: {
    name: string,
    iconUrl: string,
    trait: string,
    rarity: string,
    rarity_color: string,
    text: {
      letters: string,
      rotation: number,
    }[],
  }[][] = await fetch(`http://api.cs-tracker.com:8000/suggest/${word}`).then(res => res.json());
  console.log(stickers);

  return {
    word,
    stickers: stickers,
  };
};