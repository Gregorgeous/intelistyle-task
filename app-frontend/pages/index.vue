<template>
	<div class="container">
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
				class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r cursor-pointer">
				Prev
			</button>
			<button @click="goToNextPage"
				v-if="hasNextPage"
				class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r  cursor-pointer">
				Next
			</button>
		</div>
	</div>
</template>

<script>
import garmentCard from '~/components/garmentCard.vue'

export default {
  // In Nuxt I can use fetch instead of mounted (more SSR-friendly).
  fetch({ store, query }) {
    // On page load, spin up the Axios call to our Django Rest API backend (Our backend serves as a microservice between the Amazon data and the front-end.). This will populate our Vuex store.
    // The conditional below handles the pagination done by our backend API.
    if (!query.page) {
      return store.dispatch('fetchAllGarments')
    } else {
      return store.dispatch('fetchAllGarments', query.page)
    }
  },
  components: {
    garmentCard
  },
  computed: {
    // ----  computed properties for Vuex state values ----
    // Render the all the garment objects array from vuex. This array was populated via our fetch() on pageload. This is a "Component -> Vuex -> Component" communication pattern which might be an overkill for just 1-2 pages but is a desired, scalable design guide for Vue/React apps using Vuex/Redux (i.e. central state store mechanism)
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
      this.getNewGarments()
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
    }
  },
  methods: {
    getNewGarments() {
      if (!this.$route.query.page) {
        return this.$store.dispatch('fetchAllGarments')
      } else {
        return this.$store.dispatch('fetchAllGarments', this.$route.query.page)
      }
    },
    goToPrevPage() {
      this.$router.push({ query: { page: this.prevPageNumber } })
    },
    goToNextPage() {
      this.$router.push({ query: { page: this.nextPageNumber } })
    }
  },

  async mounted() {}
}
</script>

<style lang='scss' scoped>
@import '~/assets/scss/commonStyles.scss';
</style>
