<!-- frontend/src/App.vue -->
<template>
  <div class="app-container">
    <!-- 侧边栏菜单 -->
    <aside class="sidebar">
      <div class="logo">
        <h1>CompAssistant</h1>
      </div>
      <nav class="menu">
        <a 
          href="#" 
          @click.prevent="currentView = 'competitions'"
          :class="['menu-item', { active: currentView === 'competitions' }]"
        >
          <span class="icon">📋</span>
          <span class="text">竞赛列表</span>
        </a>
        <a 
          href="#" 
          @click.prevent="currentView = 'favorites'"
          :class="['menu-item', { active: currentView === 'favorites' }]"
        >
          <span class="icon">❤️</span>
          <span class="text">我的收藏</span>
        </a>
        <a 
          href="#" 
          @click.prevent="currentView = 'guide'"
          :class="['menu-item', { active: currentView === 'guide' }]"
        >
          <span class="icon">📖</span>
          <span class="text">竞赛指导</span>
        </a>
      </nav>
    </aside>

    <!-- 主内容区 -->
    <main class="main-content">
      <div v-if="currentView === 'competitions'" class="view">
        <CompetitionList />
      </div>
      <div v-if="currentView === 'favorites'" class="view">
        <FavoritesView />
      </div>
      <div v-if="currentView === 'guide'" class="view">
        <Guide />
      </div>
    </main>
  </div>
</template>

<script>
import { ref } from 'vue'
import CompetitionList from './components/CompetitionList.vue'
import FavoritesView from './components/FavoritesView.vue'
import Guide from './components/Guide.vue'

export default {
  name: 'App',
  components: {
    CompetitionList,
    FavoritesView,
    Guide
  },
  setup() {
    const currentView = ref('competitions')
    return { currentView }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #ffffff;
  color: #1d1d1f;
}

.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}

.sidebar {
  width: 220px;
  background-color: #f5f5f7;
  border-right: 1px solid #d2d2d7;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  overflow-y: auto;
}

.logo {
  margin-bottom: 32px;
}

.logo h1 {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.5px;
  color: #1d1d1f;
}

.menu {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 8px;
  text-decoration: none;
  color: #1d1d1f;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 4px;
}

.menu-item:hover {
  background-color: #e8e8ed;
}

.menu-item.active {
  background-color: #ffffff;
  box-shadow: inset 0 0 0 1px #d2d2d7;
  font-weight: 600;
}

.menu-item .icon {
  font-size: 18px;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  background-color: #ffffff;
}

.view {
  width: 100%;
  height: 100%;
}
</style>