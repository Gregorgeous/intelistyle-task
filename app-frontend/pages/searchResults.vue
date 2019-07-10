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
    },
    // ---- computed properties for helper display logic ----
    hasNextPage() {
      if (
        this.garmentsDisplayProperties.next != null &&
        this.garmentsDisplayProperties.next != undefined
      ) {
        return true
      } else {
        return false
      }
    },
    hasPrevPage() {
      if (
        this.garmentsDisplayProperties.previous != null &&
        this.garmentsDisplayProperties.previous != undefined
      ) {
        return true
      } else {
        return false
      }
    },
    prevPageNumber() {
      if (this.garmentsDisplayProperties.previous) {
        var url = this.garmentsDisplayProperties.previous
        let query
        try {
          query = /page=([^&]+)/.exec(url)[1]
        } finally {
          return query ? query : '1'
        }
      } else {
        return '1'
      }
    },
    nextPageNumber() {
      if (this.garmentsDisplayProperties.next) {
        var url = this.garmentsDisplayProperties.next
        var captured = /page=([^&]+)/.exec(url)[1]
        return captured ? captured : '1'
      } else {
        return '1'
      }
    }
  }
}
</script>

<style lang='scss' scoped>
@import '~/assets/scss/commonStyles.scss';
</style>
