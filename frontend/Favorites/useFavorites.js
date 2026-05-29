// frontend/src/composables/useFavorites.js
import { ref, watch } from 'vue'

const STORAGE_KEY = 'compassistant_favorites'

function loadFavorites() {
  const stored = localStorage.getItem(STORAGE_KEY)
  if (stored) {
    try {
      return new Set(JSON.parse(stored))
    } catch (e) {
      return new Set()
    }
  }
  return new Set()
}

function saveFavorites(set) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...set]))
}

export function useFavorites() {
  const favoriteIds = ref(loadFavorites())

  watch(favoriteIds, (newSet) => {
    saveFavorites(newSet)
  }, { deep: true })

  function isFavorite(id) {
    return favoriteIds.value.has(id)
  }

  function addFavorite(id) {
    favoriteIds.value.add(id)
  }

  function removeFavorite(id) {
    favoriteIds.value.delete(id)
  }

  function toggleFavorite(id) {
    if (isFavorite(id)) {
      removeFavorite(id)
    } else {
      addFavorite(id)
    }
  }

  return {
    favoriteIds,
    isFavorite,
    addFavorite,
    removeFavorite,
    toggleFavorite
  }
}