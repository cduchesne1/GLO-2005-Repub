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

const createTask = async (task) => {
  clean(task);
  if (Object.keys(task).length > 0) {
    try {
      await fetch(`${process.env.VUE_APP_API_URL}/tasks`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
      });
    } catch (error) {
      console.error(error);
    }
  }
};

const updateTask = async (taskId, task) => {
    clean(task);
    if (Object.keys(task).length > 0) {
        try {
        await fetch(`${process.env.VUE_APP_API_URL}/tasks/${taskId}`, {
            method: "PUT",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(task),
        });
        } catch (error) {
        console.error(error);
        }
    }
};

const sendNewComment = async (taskId, comment) => {
    clean(comment);
    if (Object.keys(comment).length > 0) {
        try {
        await fetch(`${process.env.VUE_APP_API_URL}/tasks/${taskId}/comments`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(comment),
        });
        } catch (error) {
        console.error(error);
        }
    }
};

const updateComment = async (commentId, comment) => {
    clean(comment);
    if (Object.keys(comment).length > 0) {
        try {
        await fetch(`${process.env.VUE_APP_API_URL}/comments/${commentId}`, {
            method: "PUT",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(comment),
        });
        } catch (error) {
        console.error(error);
        }
    }
};

const deleteComment = async (commentId) => {
    try {
        await fetch(`${process.env.VUE_APP_API_URL}/comments/${commentId}`, {
        method: "DELETE",
        });
    } catch (error) {
        console.error(error);
    }
};

// From https://stackoverflow.com/questions/286141/remove-blank-attributes-from-an-object-in-javascript
function clean(obj) {
  for (var propName in obj) {
    if (obj[propName] === null || obj[propName] === undefined) {
      delete obj[propName];
    }
  }
  return obj;
}

export {
  fetchRepositoryTasks,
  fetchUserTasks,
  fetchTaskByUsernameRepositoryAndNumber,
  fetchTaskComments,
  createTask,
  updateTask,
  sendNewComment,
  updateComment,
  deleteComment
};
