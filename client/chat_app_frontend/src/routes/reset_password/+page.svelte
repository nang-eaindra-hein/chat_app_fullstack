<script lang="ts">
  import { goto } from "$app/navigation";

  let confirmNewPassword = $state("");
  let newPassword = $state("");
  let emailInput = $state("");
  let emailCorrect = $state(false);
  let sendEmailInput = $state(false);
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
    {#if emailCorrect}
      <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">
        Reset Password
      </h1>
      <input
        bind:value={newPassword}
        type="text"
        placeholder="new password"
        class="w-full h-8 rounded-lg px-2"
      />
      <input
        bind:value={confirmNewPassword}
        type="text"
        placeholder="confirm new password"
        class="w-full h-8 rounded-lg px-2"
      />

      <button
        class="bg-green-500 rounded-lg py-1 text-white"
        onclick={() => goto("/login")}>Save</button
      >
    {:else}
      <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">
        Verify your email
      </h1>
      <input
        bind:value={emailInput}
        type="text"
        placeholder="email"
        class="w-full h-8 rounded-lg px-2"
      />

      <button
        class="bg-green-500 rounded-lg py-1 text-white"
        onclick={() => (sendEmailInput = true)}>Get PIN</button
      >
      {#if sendEmailInput}
        <div>pin</div>
        <button
          class="bg-green-500 rounded-lg py-1 text-white"
          onclick={() => (emailCorrect = true)}>Send</button
        >
      {/if}
    {/if}
  </div>

  <a href="/login" class="underline text-yellow-500">Go back to Login</a>
</div>
