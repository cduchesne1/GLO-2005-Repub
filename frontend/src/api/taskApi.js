const fetchRepositoryTasks = async (repositoryId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/repositories/${repositoryId}/tasks`
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
      `${process.env.VUE_APP_API_URL}/users/${userId}/tasks`
    );

    const data = await response.json();

    const tasks = data.tasks;
    tasks.sort((a, b) => a.number - b.number);

    return tasks;
  } catch (error) {
    console.error(error);
  }
};

const fetchTaskByUsernameRepositoryAndNumber = async (
  username,
  repository,
  number
) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${repository}/tasks/${number}`
    );

    const task = await response.json();

    return task;
  } catch (error) {
    console.error(error);
  }
};

const fetchTaskComments = async (taskId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/tasks/${taskId}/comments`
    );

    const data = await response.json();

    const comments = data.comments;
    comments.sort((a, b) => ("" + a.timestamp).localeCompare("" + b.timestamp));

    return comments;
  } catch (error) {
    console.error(error);
  }
};

export {
  fetchRepositoryTasks,
  fetchUserTasks,
  fetchTaskByUsernameRepositoryAndNumber,
  fetchTaskComments,
};
