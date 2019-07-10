import axios from '~/plugins/myApiAxios'

export const state = () => ({
  garmentDisplayProperties: {},
  garmentDetails: {}
})

export const mutations = {
  UPDATE_GARMENT_DISPLAY_PROPERTIES(state, payload) {
    let properties = {
      count: payload.count,
      next: payload.next,
      previous: payload.previous
    }
    state.garmentDisplayProperties = properties
  },
  UPDATE_GARMENTS(state, payload) {
    state.garments = payload
  },
}
