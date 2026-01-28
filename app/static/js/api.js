const API_BASE = '/api';

const newsApi = {
    getAll: async (skip = 0, limit = 100) => {
        try {
            const response = await fetch(`${API_BASE}/news/?skip=${skip}&limit=${limit}`);
            if (!response.ok) throw new Error('Failed to fetch news');
            return await response.json();
        } catch (error) {
            console.error('Error fetching news:', error);
            return [];
        }
    },
    getById: async (id) => {
        try {
            const response = await fetch(`${API_BASE}/news/${id}`);
            if (!response.ok) throw new Error('Failed to fetch news item');
            return await response.json();
        } catch (error) {
            console.error(`Error fetching news ${id}:`, error);
            return null;
        }
    }
};

const courseApi = {
    getAll: async (skip = 0, limit = 100) => {
        try {
            const response = await fetch(`${API_BASE}/courses/?skip=${skip}&limit=${limit}`);
            if (!response.ok) throw new Error('Failed to fetch courses');
            return await response.json();
        } catch (error) {
            console.error('Error fetching courses:', error);
            return [];
        }
    }
};

const resourceApi = {
    getCategories: async () => {
        try {
            const response = await fetch(`${API_BASE}/resources/categories`);
            if (!response.ok) throw new Error('Failed to fetch categories');
            return await response.json();
        } catch (error) {
            console.error('Error fetching categories:', error);
            return [];
        }
    },
    getAll: async (skip = 0, limit = 100) => {
        try {
            const response = await fetch(`${API_BASE}/resources/?skip=${skip}&limit=${limit}`);
            if (!response.ok) throw new Error('Failed to fetch resources');
            return await response.json();
        } catch (error) {
            console.error('Error fetching resources:', error);
            return [];
        }
    }
};

const pathwayApi = {
    getAll: async (skip = 0, limit = 100) => {
        try {
            const response = await fetch(`${API_BASE}/pathways/?skip=${skip}&limit=${limit}`);
            if (!response.ok) throw new Error('Failed to fetch pathways');
            return await response.json();
        } catch (error) {
            console.error('Error fetching pathways:', error);
            return [];
        }
    },
    getBySlug: async (slug) => {
        try {
            const response = await fetch(`${API_BASE}/pathways/${slug}`);
            if (!response.ok) throw new Error('Failed to fetch pathway');
            return await response.json();
        } catch (error) {
            console.error(`Error fetching pathway ${slug}:`, error);
            return null;
        }
    },
    create: async (pathwayData) => {
        try {
            const response = await fetch(`${API_BASE}/pathways/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(pathwayData)
            });
            if (!response.ok) throw new Error('Failed to create pathway');
            return await response.json();
        } catch (error) {
            console.error('Error creating pathway:', error);
            return null;
        }
    }
};
