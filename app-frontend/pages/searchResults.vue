<template>
	<div class="container">
		<h1 class="mb-6"
			v-if="$route.query">Your search results for:
			<span class="text-xl uppercase font-bold">{{$route.query.q}}</span>
		</h1>
		<div class="garments-grid">
			<template v-for="(item, index) in allGarments">
				<garmentCard :garmentObject=item
					:key="index"></garmentCard>
			</template>
		</div>
	</div>
</template>

<script>
import garmentCard from '~/components/garmentCard.vue'

export default {
  // In Nuxt I can use fetch instead of mounted (more SSR-friendly).
  fetch({ store, query, redirect }) {
    if (!query.q) {
      // if there's nothing in the search query, simply redirect to the main page.
      return redirect('/')
    } else {
      return store.dispatch('searchGarment', query.q)
    }
  },
  components: {
    garmentCard
  },
  computed: {
    // ----  computed properties for Vuex state values ----
    allGarments() {
      return this.$store.state.garments
    },
    garmentsDisplayProperties() {
      return this.$store.state.garmentDisplayProperties
    }
  }
}
</script>

<style lang='scss' scoped>
@import '~/assets/scss/commonStyles.scss';
</style>
