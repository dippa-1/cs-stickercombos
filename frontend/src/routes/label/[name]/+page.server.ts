import { error, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';
export const actions = {
    default: async ({ request, params }) => {
        const data = await request.formData();
        const labels = data.getAll('label').filter(l => !!l?.toString()?.length);
        if (!labels.length) {
            error(400, 'No labels provided');
        }

        const name = params.name;
        if (!name?.length) {
            error(400, 'No name provided');
        }

        const response = await fetch(`http://localhost:5000/label/${name}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ labels, rotation: 0 }),
        });
        if (response.status !== 201) {
            error(500, 'Failed to label');
        }
        console.log('Labeling response', response);
        redirect(301, `/label`)
    },
} satisfies Actions;