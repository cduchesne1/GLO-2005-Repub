const fetchRepositoryTasks = async (repositoryId) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/repositories/${repositoryId}/tasks`,
        );

        const data = await response.json();

        const tasks = data.tasks;
        tasks.sort((a, b) => a.number - b.number);

        return tasks;
    } catch (error) {
        console.error(error);
    }
};

const fetchUserTasks = async (userId) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/users/${userId}/tasks`,
        );

        const data = await response.json();

        const tasks = data.tasks;
        tasks.sort((a, b) => a.number - b.number);

        return tasks;
    } catch (error) {
        console.error(error);
    }
};

export { fetchRepositoryTasks, fetchUserTasks };