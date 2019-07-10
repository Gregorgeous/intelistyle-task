<template>
	<nav class="flex items-center justify-between flex-wrap bg-gray-800 p-2">
		<div @click="navigateHome"
			class="flex items-center flex-shrink-0 text-white mr-6 cursor-pointer ">
			<img src="~/assets/images/logo_test.png"
				id="website-logo"
				alt="Intelistyle logo">
		</div>
		<div class="block">
			<form class="w-full max-w-sm"
				@submit.prevent='searchGarment'>
				<div class="flex items-center py-2">
					<input id="search__input"
						class="appearance-none bg-transparent border-b w-full text-white py-1 px-2 leading-tight focus:outline-none z-0"
						type="text"
						v-model="searchQuery"
						placeholder="Black dress"
						aria-label="Searchbox for a garment">
					<button id="searchBtn"
						class="bg-gray-800 border border-white-500 hover:bg-white hover:text-gray-800 text-white font-bold py-2 px-4 z-10 rounded-full">
						Search
					</button>
				</div>
			</form>
		</div>
	</nav>
</template>


<script>
export default {
  data() {
    return {
      searchQuery: ''
    }
  },
  methods: {
    searchGarment() {
      if (this.searchQuery === '') {
        this.$router.push('/')
      } else {
        this.$router.push({
          name: 'searchResults',
          query: { q: this.searchQuery }
        })
      }
    },
    navigateHome() {
      this.$router.push('/')
    }
  }
}
</script>


<style lang='scss' scoped>
#search__input {
  transform: translateY(7px) translateX(20px);
  transition: border-radius 0.2s ease-in, transform 0.2s ease-in,
    border-bottom 0.2s ease-in;
  &:focus {
    border-bottom: 3px solid white;
    border-radius: 7px;
    transform: translateY(5px) translateX(20px);
  }
}

#searchBtn {
  transition: all 0.2s ease;
}

#website-logo {
  width: 73px;
  margin-left: 35px;
  filter: invert(1);
  transition: filter 0.1s ease;
  &:hover {
    filter: invert(1) drop-shadow(2px 4px 4px white);
  }
}
</style>
