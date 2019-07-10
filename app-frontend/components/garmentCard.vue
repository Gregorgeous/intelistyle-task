<template>
	<div class="garment-card max-w-sm rounded overflow-hidden shadow-lg hover:shadow-xl hover:border-4 ">
		<img class="w-full garment-card__image"
			:src="garmentObject.picture"
			alt="Women in a black coat">
		<div class="garment-card__name font-bold text-white text-base md:text-xl mb-2 opacity-75">{{garmentObject.name}}</div>
		<div class="garment-card__description text-gray-200 text-base opacity-75">
			{{garmentObject.description}}
		</div>
	</div>
</template>

<script>
export default {
  props: ['garmentObject']
}
</script>

<style lang='scss' scoped>
</style>
