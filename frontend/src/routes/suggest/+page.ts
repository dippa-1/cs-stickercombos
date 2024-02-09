import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ url }) => {
  const word = url.searchParams.get('word');
  console.log({ word })
  if (!word?.length) {
    return error(400, 'No word provided.')
  }
  return {
    word,
  };
};