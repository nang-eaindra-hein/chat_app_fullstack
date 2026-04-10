<script lang="ts">
  import { goto } from "$app/navigation";
  import { createMutation } from "@tanstack/svelte-query";
  import type { LoginPayload, LoginResponse } from "$lib/type";
  import { loginUser } from "$lib/api";

  let loginUsername = $state("");
  let loginPassword = $state("");
  let message = $state("");

  const loginMutation = createMutation<LoginResponse, Error, LoginPayload>(
    () => ({
      mutationFn: loginUser,
      onSuccess: async (data) => {
        localStorage.setItem("token", data.access_token);
        message = "Login successful!";
        await goto("/chat");
      },
      onError: (error: any) => {
        message =
          error?.response?.data?.detail || error?.message || "Login failed";
      },
    })
  );

  function handleLogin() {
    if (!loginUsername || !loginPassword) {
      message = "Please fill all fields";
      return;
    }

    loginMutation.mutate({
      login: loginUsername,
      password: loginPassword,
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
    class=" min-w-70 max-w-70 space-y-4 shadow-lg p-4 rounded-lg flex flex-col"
  >
    <div class="flex">
      <img src="/beelogo.png" alt="beelogo" class="w-15 h-15" />
      <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">Log In</h1>
    </div>
    <input
      bind:value={loginUsername}
      type="text"
      placeholder="username or email"
      class="w-full h-8 rounded-lg px-2"
    />
    <input
      bind:value={loginPassword}
      type="password"
      placeholder="password"
      class="w-full h-8 rounded-lg px-2"
    />

    <button
      class="bg-green-500 rounded-lg py-1 text-white disabled:opacity-50"
      onclick={handleLogin}
      disabled={loginMutation.isPending}
    >
      {loginMutation.isPending ? "Logging in..." : "Log In"}
    </button>
    {#if message}
      <p class="text-yellow-500 text-sm flex justify-center items-center">
        {message}
      </p>
    {/if}
  </div>
  <a href="/" class="underline text-yellow-500">Don't have an account? Signup</a
  >
  <a href="/reset_password" class="underline text-yellow-500"
    >Forgot your password?</a
  >
</div>
