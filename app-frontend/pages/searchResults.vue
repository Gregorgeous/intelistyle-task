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
		<div class="pagination-btns-group inline-flex"
			v-if="hasNextPage || hasPrevPage">
			<button @click="goToPrevPage"
				v-if="hasPrevPage"
				class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r">
				Previous results
			</button>
			<button @click="goToNextPage"
				v-if="hasNextPage"
				class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r">
				More found
			</button>
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
  },
  watch: {
    $route() {
      if (!this.$route.query || !this.$route.query.q) {
        return this.$router.push('/')
      }
      this.getNextFoundGarments()
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
    }
  },
  methods: {
    getNextFoundGarments() {
      let payload = {
        page: this.$route.query.page ? this.$route.query.page : '1',
        q: this.$route.query.q
      }
      return this.$store.dispatch('searchPaginatedGarment', payload)
    },
    goToPrevPage() {
      this.$router.push({
        query: { page: this.prevPageNumber, q: this.$route.query.q }
      })
    },
    goToNextPage() {
      this.$router.push({
        query: { page: this.nextPageNumber, q: this.$route.query.q }
      })
    }
  }
}
</script>

<style lang='scss' scoped>
@import '~/assets/scss/commonStyles.scss';
</style>
