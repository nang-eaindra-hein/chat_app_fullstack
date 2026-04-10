<script lang="ts">
  import "../layout.css";
  let { children } = $props();
  import { QueryClient } from "@tanstack/svelte-query";
  import { QueryClientProvider } from "@tanstack/svelte-query";
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        refetchOnWindowFocus: false,
      },
    },
  });
</script>

<QueryClientProvider client={queryClient}>
  {@render children()}
</QueryClientProvider>
