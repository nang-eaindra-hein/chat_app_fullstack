<script lang="ts">
  import { goto } from "$app/navigation";
  import {
    createMutation,
    createQuery,
    useQueryClient,
  } from "@tanstack/svelte-query";
  import { getUser, updateChangesPatch } from "$lib/api";
  import type { updateResponse, GetUserPayload } from "$lib/type";
  import axios from "axios";
  import { idText } from "typescript";

  let editUsername = $state(false);
  let usernameValue = $state<string | undefined>("");

  let editEmail = $state(false);
  let emailValue = $state<string | undefined>("");

  let editNumber = $state(false);
  let numberValue = $state<string | undefined>("");
  //get user Query
  const getUserQuery = createQuery<GetUserPayload>(() => ({
    queryKey: ["getUser"],
    queryFn: getUser,
  }));

  //update mutation
  const queryClient = useQueryClient();
  const updateMutation = createMutation((data: Partial<updateResponse>) => ({
    mutationFn: updateChangesPatch,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["updateChanges"] });
    },
  }));

  //delete account
  function handleDeleteAccount() {}

  //save changes
  function handleSave() {
    updateMutation.mutate({});
  }

  function handleEditUsername() {
    editUsername = true;
    usernameValue = getUserQuery.data?.username;
  }

  function handleEditEmail() {
    editEmail = true;
    emailValue = getUserQuery.data?.email;
  }

  function handleEditNumber() {
    editNumber = true;
    numberValue = getUserQuery.data?.number;
  }
</script>

<img
  src="/bee.png"
  alt="bee-bg"
  class="relative z-0 w-full h-screen shrink-0 object-cover"
/>

<div
  class="absolute top-0 z-10 w-screen min-h-screen flex flex-col space-y-4 justify-center items-center font-turncoat"
>
  <div
    class=" min-w-90 max-w-90 space-y-4 shadow-lg p-4 rounded-lg flex flex-col"
  >
    <button
      class="shadow-xl bg-yellow-100 rounded-lg py-1 text-black px-6 w-fit justify-start items-start"
      onclick={() => goto("/chat")}>Back</button
    >
    <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">Profile</h1>

    <div class="flex justify-center items-center">
      <img
        src="/beelogo.png"
        alt="avatar"
        class="w-15 h-15 border rounded-full bg-yellow-50"
      />
    </div>
    <!--id-->
    <p>id :<span class="pl-2 text-green-500">{getUserQuery.data?.id}</span></p>

    <!--username-->
    <span class="flex justify-between">
      Username : <span
        class="text-yellow-500 {editUsername ? 'hidden' : 'flex'} "
        >{getUserQuery.data?.username}</span
      >
      <input
        type="text"
        class=" {editUsername ? 'flex' : 'hidden'} "
        bind:value={usernameValue}
      />
      <button
        onclick={handleEditUsername}
        class="bg-yellow-50 cursor-pointer rounded-lg p-1 border text-sm border-amber-300"
        >Edit</button
      >
    </span>
    <!--email-->
    <span class="flex justify-between">
      Email :<span class="text-yellow-500 {editEmail ? 'hidden' : 'flex'} "
        >{getUserQuery.data?.email}</span
      >
      <input
        type="text"
        class=" {editEmail ? 'flex' : 'hidden'} "
        bind:value={emailValue}
      />
      <button
        onclick={handleEditEmail}
        class="bg-yellow-50 cursor-pointer rounded-lg p-1 border text-sm border-amber-300"
        >Edit</button
      >
    </span>
    <!--number-->
    <span class="flex justify-between">
      contact number :
      <span class="text-yellow-500 {editNumber ? 'hidden' : 'flex'} "
        >{getUserQuery.data?.number}</span
      >
      <input
        type="text"
        class=" {editNumber ? 'flex' : 'hidden'} "
        bind:value={numberValue}
      />

      <button
        onclick={handleEditNumber}
        class="bg-yellow-50 cursor-pointer rounded-lg p-1 border text-sm border-amber-300"
        >Edit</button
      >
    </span>
    <!--save-->
    <button
      onclick={handleSave}
      class="bg-green-500 cursor-pointer rounded-lg py-1 text-white"
      >Save</button
    >
    <!--delete-->
    <button
      onclick={handleDeleteAccount}
      class="bg-red-500 rounded-lg py-1 text-white cursor-pointer"
      >Delete an account</button
    >
  </div>
</div>
