<script lang="ts">
  import { goto } from "$app/navigation";
  import { getUsers } from "$lib/api";
  import type { GetUserPayload } from "$lib/type";
  import { createQuery } from "@tanstack/svelte-query";

  const getUsersQuery = createQuery<GetUserPayload>(() => ({
    queryKey: ["getUsers"],
    queryFn: getUsers,
  }));

  let inbox = $state([
    {
      user: "o",
      name: getUsersQuery.data?.username ?? "-",
      text: "yj",
      date: "2/3/4",
      read: false,
    },
  ]);

  let eachNameChatOpen = $state("");
  let eachUserChatOpen = $state("");
  let profileOpenModal = $state(false);
</script>

<div class="grid grid-cols-4 h-screen overflow-hidden font-turncoat">
  <!--left-->
  <div class="col-span-1 bg-yellow-200">
    <h1
      class="text-2xl text-yellow-500 text-center py-2 w-full bg-yellow-100 border-b border-b-white"
    >
      <button
        onclick={() => {
          profileOpenModal = !profileOpenModal;
        }}
        class="absolute z-30 top-0 left-0"
      >
        <img src="/beelogo.png" alt="logo" class=" w-15 h-15" /></button
      > Inbox
    </h1>
    {#if profileOpenModal}
      <div
        class="bg-white absolute z-40 left-0 rounded-xl shadow-lg p-2 min-w-40 max-w-40"
      >
        <button
          class="w-full py-1 px-2 hover:bg-yellow-100 rounded-lg"
          onclick={() => {
            goto("/profile");
          }}>Profile</button
        >
        <button
          class="w-full py-1 px-2 hover:bg-yellow-100 rounded-lg"
          onclick={() => {
            goto("/settings");
          }}>Settings</button
        >
        <button
          onclick={() => {
            goto("/login");
          }}
          class="w-full py-1 px-2 hover:bg-yellow-100 rounded-lg"
          >Log Out</button
        >
      </div>
    {/if}
    {#each inbox as box}
      <button
        onclick={() => {
          eachNameChatOpen = box.name;
        }}
        class="border-b border-yellow-500 {eachNameChatOpen !== box.name
          ? 'bg-yellow-100 hover:bg-yellow-200'
          : 'bg-yellow-200 '}  space-y-2 w-full px-6 py-4"
      >
        <div class="flex justify-between w-full">
          <div class="flex gap-2">
            <h1>{box.user}</h1>
            <p>{box.name}</p>
          </div>
          <p>{box.date}</p>
        </div>
        <p class="text-start {box.read ? ' text-black' : 'text-gray-400'} ">
          {box.text}
        </p>
      </button>
    {/each}
  </div>
  <!--right-->
  <div class="col-span-3 w-full h-screen relative">
    <img src="/bee.png" alt="bee-bg" class=" z-0 shrink-0 object-cover" />
    <div
      class="absolute z-10 top-0 w-full right-0 bg-amber-100 border-b border-white text-center"
    >
      <div
        class="flex px-6 justify-center gap-2 {!eachNameChatOpen
          ? ''
          : 'border-b py-3  border-white bg-yellow-100'}"
      >
        <h1 class="">{eachUserChatOpen}</h1>
        <p class="">{eachNameChatOpen}</p>
      </div>
      <!--keyboard-->
    </div>
  </div>
</div>
