const fetchUserRecentRepositories = async (userId) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/users/${userId}/repositories`,
        );

        const data = await response.json();

        const repositories = data.repositories;
        repositories.sort((a, b) => a.id - b.id);

        return repositories.slice(0, 5);
    } catch (error) {
        console.error(error);
    }
};

const fetchUserRepositories = async (userId) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/users/${userId}/repositories`,
        );

        const data = await response.json();

        const repositories = data.repositories;
        repositories.sort((a, b) => a.id - b.id);

        return repositories;
    } catch (error) {
        console.error(error);
    }
};

const fetchExploreRepositories = async () => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/repositories`,
        );

        const data = await response.json();

        const repositories = data.repositories;

        return shuffle(repositories);
    } catch (error) {
        console.error(error);
    }
};

const fetchRepository = async (repositoryId) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/repositories/${repositoryId}`,
        );

        const repository = await response.json();

        return repository;
    } catch (error) {
        console.error(error);
    }
};

const fetchRepositoryByUsernameAndName = async (username, name) => {
    try {
        const response = await fetch(
            `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${name}`,
        );

        const repository = await response.json();

        return repository;
    } catch (error) {
        console.error(error);
    }
};

// From https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array?page=1&tab=trending#tab-top
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }

export { fetchUserRecentRepositories, fetchUserRepositories, fetchExploreRepositories, fetchRepository, fetchRepositoryByUsernameAndName };