import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ url }) => {
  const word = url.searchParams.get('word');
  if (!word?.length) {
    return error(400, 'No word provided.')
  }

  const res: {
    name: string,
    iconUrl: string,
    rarity: string,
    letters: string,
  }[] = await fetch(`http://localhost:5000/suggest/${word}`).then(res => res.json());
  console.log(res);

  return {
    word,
    res,
  };
};