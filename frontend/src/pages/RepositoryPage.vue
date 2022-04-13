<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex flex-col flex-1 px-16">
      <div class="flex items-center">
        <h1 class="text-2xl text-pink-600">johndoe1</h1>
        <h1 class="text-2xl text-gray-500 mx-2">/</h1>
        <h1 class="text-2xl text-pink-600 font-bold">HELLO</h1>
        <div
          class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4"
        >
          Private
        </div>
      </div>
      <TabsComponent class="mt-8">
          <TabComponent name="Code" :selected="true">
              <CodeTab />
          </TabComponent>
          <TabComponent name="Tasks" :selected="false">
              <TasksTab />
          </TabComponent>
          <TabComponent name="Settings" :selected="false">
              <SettingsTab />
          </TabComponent>
      </TabsComponent>
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import TabsComponent from "@/components/TabsComponent";
import TabComponent from "@/components/TabComponent";
import CodeTab from "@/components/repository/CodeTab";
import TasksTab from "@/components/repository/TasksTab";
import SettingsTab from "@/components/repository/SettingsTab";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
    TabsComponent,
    TabComponent,
    CodeTab,
    TasksTab,
    SettingsTab,
  },
  data() {
    return {};
  },
};
</script>
