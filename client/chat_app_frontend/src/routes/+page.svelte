<script lang="ts">
  import { createMutation } from "@tanstack/svelte-query";
  import type { SignupPayload } from "$lib/type";
  import { signupUser } from "$lib/api";
  import { goto } from "$app/navigation";

  let signupUsername = $state("");
  let signupPassword = $state("");
  let signupEmail = $state("");
  let message = $state("");
  let signupNumber = $state("");

  // mutation
  const signupMutation = createMutation(() => ({
    mutationFn: (data: SignupPayload) => signupUser(data),
    onSuccess: async () => {
      message = "SignUp Successful!";
      await goto("/login");
    },
    onError: (error: any) => {
      message =
        error?.response?.data?.detail || error?.message || "SignUp failed";
    },
  }));

  function handleSignup() {
    signupMutation.mutate({
      username: signupUsername,
      email: signupEmail,
      password: signupPassword,
      number: signupNumber,
    });
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
  <h1 class="font-turncoat text-4xl font-semibold text-yellow-500">
    Welcome to BeeChat!
  </h1>
  <p class="font-turncoat text-2xl text-yellow-400">
    Enjoy every chat with beechat.
  </p>
  <div
    class="min-w-70 max-w-70 space-y-4 shadow-lg p-4 rounded-lg flex flex-col"
  >
    <div class="flex items-center">
      <img src="/beelogo.png" alt="beelogo" class="w-15 h-15" />
      <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">Sign Up</h1>
    </div>
    <input
      required
      bind:value={signupUsername}
      type="text"
      placeholder="username"
      class="w-full h-8 rounded-lg px-2"
    />

    <input
      required
      bind:value={signupEmail}
      type="text"
      placeholder="Email"
      class="w-full h-8 rounded-lg px-2"
    />

    <input
      required
      bind:value={signupPassword}
      type="password"
      placeholder="password"
      class="w-full h-8 rounded-lg px-2"
    />
    <input
      required
      bind:value={signupNumber}
      type="text"
      placeholder="contact number"
      class="w-full h-8 rounded-lg px-2"
    />

    <button
      onclick={handleSignup}
      disabled={signupMutation.isPending}
      class="bg-green-500 rounded-lg py-1 text-white"
    >
      {signupMutation.isPending ? "Signing..." : "Sign Up"}
    </button>

    {#if message}
      <p class="text-yellow-500 flex justify-center items-center text-sm">
        {message}
      </p>
    {/if}
  </div>

  <a href="/login" class="underline text-yellow-500">
    Have an account? Login
  </a>
</div>
