import type { PageLoad } from "./$types";

export const csr = false;

export const load: PageLoad = async ({ url }) => {
  const word = url.searchParams.get('word');
  if (!word?.length) {
  }

  return {
    word,
  };
};