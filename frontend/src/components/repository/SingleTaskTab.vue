<template>
  <div class="flex flex-col mt-16">
    <div
      v-if="task"
      class="flex flex-col border-b border-solid border-gray-500 pb-4"
    >
      <div class="flex justify-between w-full">
        <div class="flex items-center mb-2">
          <h2 v-if="!editTitle" class="text-4xl text-white mr-4">
            {{ task.title }}
          </h2>
          <input
            v-if="editTitle"
            type="text"
            v-model="title"
            @keyup.enter="onEnter"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg mr-4"
          />
          <h2 class="text-4xl text-gray-500">{{ `#${task.number}` }}</h2>
        </div>
        <div class="flex items-center">
          <button
            @click="setEditTitle()"
            class="bg-gray-500 hover:bg-gray-600 text-white text-sm font-bold py-1 px-4 rounded mx-4 h-8"
          >
            Edit
          </button>
          <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded h-8 w-24"
            @click="createNewTask()"
          >
            New task
          </button>
        </div>
      </div>
      <div class="flex items-center">
        <div
          class="bg-green-500 rounded-full py-2 px-4 text-white w-16 flex justify-center mr-4"
          :class="task.state == 'closed' ? 'bg-purple-500' : ''"
        >
          {{ task.state.charAt(0).toUpperCase() + task.state.slice(1) }}
        </div>
        <a class="text-gray-500 text-base font-bold mr-2">{{
          task.creator.username
        }}</a>
        <a class="text-gray-500 text-base">{{
          `opened this task ${timeAgo(task.timestamp)} - ${
            comments.length
          } comments`
        }}</a>
      </div>
    </div>
    <div class="flex">
      <div class="flex flex-col flex-1">
        <div
          v-if="task"
          class="border border-solid border-gray-500 rounded-lg w-full mt-4"
        >
          <div class="flex bg-pink-500 bg-opacity-25 px-8 py-4 justify-between">
            <div>
              <a class="text-base text-white font-bold mr-4">{{
                task.creator.username
              }}</a>
              <a class="text-base text-gray-500">{{
                `commented ${timeAgo(task.timestamp)}`
              }}</a>
            </div>
            <div class="flex">
              <a
                @click="updateDescription()"
                v-if="editDescription"
                class="text-base text-gray-500 hover:text-pink-500 mr-4"
                >Done</a
              >
              <a
                @click="setEditDescription()"
                class="text-base text-gray-500 hover:text-pink-500"
                >{{ editDescription ? "Cancel" : "Edit" }}</a
              >
            </div>
          </div>
          <div class="text-white px-4 py-4">
            <p v-if="!editDescription" class="w-full">
              {{ task.description }}
            </p>
            <textarea
              v-if="editDescription"
              type="text"
              v-model="description"
              class="bg-gray-900 text-white w-full py-2 px-2 rounded-lg"
            />
          </div>
        </div>
        <div class="flex flex-col mt-16">
          <div
            v-for="comment in comments"
            :key="comment.id"
            class="border border-solid border-gray-500 rounded-lg w-full mt-4"
          >
            <div
              class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between"
            >
              <div>
                <a class="text-base text-white font-bold mr-4">{{
                  comment.sender.username
                }}</a>
                <a class="text-base text-gray-500">{{
                  `commented ${timeAgo(comment.timestamp)}`
                }}</a>
              </div>
              <div class="flex">
                <a
                  @click="editOneComment()"
                  v-if="editComment == comment.id"
                  class="text-base text-gray-500 hover:text-pink-500 mr-4"
                  >Done</a
                >
                <a
                  @click="setEditComment(comment.id)"
                  class="text-base text-gray-500 hover:text-pink-500"
                  >{{ editComment == comment.id ? "Cancel" : "Edit" }}</a
                >
                <a
                  @click="deleteOneComment(comment.id)"
                  class="text-base text-gray-500 hover:text-pink-500 ml-4"
                  >Delete</a
                >
              </div>
            </div>
            <div class="text-white px-4 py-4">
              <p v-if="editComment != comment.id" class="w-full">
                {{ comment.comment }}
              </p>
              <textarea
                v-if="editComment == comment.id"
                type="text"
                v-model="editCommentContent"
                class="bg-gray-900 text-white w-full py-2 px-2 rounded-lg"
              />
            </div>
          </div>
          <div
            class="border border-solid border-gray-500 rounded-lg w-full mt-8"
          >
            <div
              class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between"
            >
              <a class="text-base text-white font-bold mr-4">Leave a comment</a>
            </div>
            <div class="text-white px-4 py-4">
              <textarea
                type="text"
                v-model="newComment"
                class="bg-gray-900 text-white w-full py-2 px-2 rounded-lg"
              />
              <div class="flex items-center w-full justify-end mt-2">
                <button
                  @click="updateState()"
                  class="bg-gray-500 hover:bg-gray-600 text-white text-sm font-bold py-1 px-4 rounded mx-4 h-8"
                >
                  {{ task.state == "closed" ? "Reopen task" : "Close task" }}
                </button>
                <button
                  @click="sendComment()"
                  class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded h-8 w-24"
                  :class="newComment ? '' : 'opacity-25'"
                >
                  Comment
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        v-if="task"
        class="flex flex-col ml-16 mt-4 border-b border-solid border-gray-500 h-full pb-8"
      >
        <div class="flex justify-between w-56">
          <a class="text-base text-gray-500 font-bold">Assignee</a>
          <a
            @click="setEditAssigned()"
            class="text-base text-gray-500 hover:text-pink-500 text-right"
            >Add</a
          >
        </div>
        <a
          v-if="!task.assigned && !editAssigned"
          class="text-base text-gray-500 mt-4"
          >No one - assign yourself</a
        >
        <a
          v-if="task.assigned && !editAssigned"
          class="text-base text-gray-500 mt-4"
          >{{ task.assigned.username }}</a
        >
        <v-select
          v-if="editAssigned"
          :options="collaborators.map((c) => c.username)"
          :value="assignee"
          @input="setAssigned"
          class="branch-picker mt-4 w-48"
        >
        </v-select>
      </div>
    </div>
  </div>
</template>
<script>
import moment from "moment";
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";
import {
  fetchTaskByUsernameRepositoryAndNumber,
  fetchTaskComments,
  updateTask,
  sendNewComment,
  updateComment,
  deleteComment,
} from "@/api/taskApi";

export default {
  data() {
    return {
      task: null,
      comments: [],
      editTitle: false,
      editDescription: false,
      editComment: null,
      title: "",
      newComment: "",
      editCommentContent: "",
      description: "",
      collaborators: [],
      assignee: null,
      editAssigned: false,
    };
  },
  async created() {
    this.collaborators = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    ).then((response) => response.collaborators);
    this.task = await fetchTaskByUsernameRepositoryAndNumber(
      this.$route.params.username,
      this.$route.params.repository,
      this.$route.params.number
    );
    this.comments = await fetchTaskComments(this.task.id);
    this.title = this.task.title;
    this.assignee = this.task.assigned ? this.task.assigned.username : "";
  },
  methods: {
    createNewTask() {
      this.$router.push(
        `/${this.$route.params.username}/${this.$route.params.repository}/tasks/new`
      );
    },
    timeAgo(timestamp) {
      return moment(Date.parse(timestamp)).fromNow();
    },
    setEditTitle() {
      this.editTitle = !this.editTitle;
    },
    setEditDescription() {
      this.editDescription = !this.editDescription;
      this.description = this.task.description;
    },
    async onEnter() {
      if (this.title && this.title !== this.task.title) {
        await updateTask(this.task.id, { title: this.title });
        this.task.title = this.title;
        this.editTitle = false;
      }
    },
    async updateDescription() {
      await updateTask(this.task.id, {
        description: this.description ? this.description : null,
      });
      this.task.description = this.description;
      this.editDescription = false;
    },
    async updateState() {
      await updateTask(this.task.id, {
        state: this.task.state == "open" ? "closed" : "open",
      });
      this.task.state = this.task.state == "open" ? "closed" : "open";
    },
    setEditComment(comment) {
      if (this.editComment == comment) {
        this.editComment = null;
        this.editCommentContent = "";
      } else {
        this.editComment = comment;
        this.editCommentContent = this.comments.find(
          (c) => c.id == comment
        ).comment;
      }
    },
    async editOneComment() {
      const comment = {
        comment: this.editCommentContent,
      };
      if (this.editCommentContent) {
        await updateComment(this.editComment, comment);
        this.comments = await fetchTaskComments(this.task.id);
        this.editComment = null;
        this.editCommentContent = "";
      }
    },
    async deleteOneComment(commentId) {
      await deleteComment(commentId);
      this.comments = await fetchTaskComments(this.task.id);
    },
    async sendComment() {
      const comment = {
        sender: this.$store.user.id,
        comment: this.newComment,
      };
      if (this.newComment) {
        await sendNewComment(this.task.id, comment);
        this.comments = await fetchTaskComments(this.task.id);
        this.newComment = "";
      }
    },
    setEditAssigned() {
      this.editAssigned = !this.editAssigned;
    },
    async setAssigned(value) {
      if (value && value != this.assignee) {
        await updateTask(this.task.id, {
          assigned: this.collaborators.find((c) => c.username == value).id,
        });
        this.task.assigned = this.collaborators.find(
          (c) => c.username == value
        );
        this.assignee = value;
        this.editAssigned = false;
      }
    },
  },
};
</script>

<style scoped>
.branch-picker {
  --vs-controls-color: #eeeeee;
  --vs-border-color: rgba(107, 114, 128, 1);

  --vs-dropdown-bg: rgba(17, 24, 39, 1);
  --vs-dropdown-color: #eeeeee;
  --vs-dropdown-option-color: #eeeeee;

  --vs-selected-bg: rgba(219, 39, 119, 1);
  --vs-selected-color: #eeeeee;

  --vs-search-input-color: #eeeeee;

  --vs-dropdown-option--active-bg: rgba(219, 39, 119, 1);
  --vs-dropdown-option--active-color: #eeeeee;
}
</style>
