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
.garment-card {
  position: relative;
  cursor: pointer;
  transition: border-radius 0.2s ease-out, border 0.2s ease-out;
  border: 1px solid #e8e8e8;

  &:hover {
    border-radius: 20px;
    border: 1px solid #c8c8c8;
  }

  &__name {
    position: absolute;
    top: 0.7em;
    margin: 0;
    left: 0;
    background: #2d3748;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    height: 33px;
    padding-left: 1em;
    padding-right: 0.5em;
    width: max-content;
    display: -webkit-box;
    display: flex;
    -webkit-box-align: center;
    align-items: center;
  }

  &:hover &__description {
    left: 0;
  }

  &__description {
    position: absolute;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    display: flex;
    justify-items: center;
    align-items: center;
    margin: 0;
    bottom: calc(50% - 30px);
    text-align: center;
    background: #2d3748;
    padding: 0.7em 0.8em 0.7em 1em;
    width: fit-content;
    left: -100%;
    transition: left 0.3s ease;
  }
}
</style>
