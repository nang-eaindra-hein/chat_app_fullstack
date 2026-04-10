<script lang="ts">
  import { goto } from "$app/navigation";
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
    class=" min-w-70 max-w-70 space-y-4 shadow-lg p-4 rounded-lg flex flex-col"
  >
    <button
      class="shadow-xl bg-yellow-100 rounded-lg py-1 text-black px-6 w-fit justify-start items-start"
      onclick={() => goto("/chat")}>Back</button
    >
    <h1 class="text-3xl text-yellow-500 pb-6 font-semibold">Settings</h1>

    <button
      class="bg-green-500 rounded-lg py-1 text-white"
      onclick={() => goto("/chat")}>Save</button
    >
  </div>
</div>
