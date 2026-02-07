# CompAssistant - 大学生竞赛帮助系统

一个简约、现代的大学生竞赛截止日期管理网站。

## 功能特性

- 📋 **竞赛列表**：清晰展示竞赛名称、截止时间、领域、难度和级别
- 🔍 **智能筛选**：按竞赛领域、级别筛选，支持关键词搜索
- 📅 **DDL 提醒**：自动计算剩余天数，区分"未开始"、"进行中"和"已截止"状态
- 📖 **竞赛详情**：包含基本信息、简介、官网链接、参赛建议
- 📚 **竞赛指导**：提供选赛建议、准备指南、常见问题等内容
- 🎨 **简约设计**：简约风格的 UI，流畅的交互体验

## 技术栈

### 前端

- **Vue 3** - 渐进式 JavaScript 框架
- **Vite** - 下一代前端构建工具
- **Axios** - HTTP 客户端

### 后端

- **FastAPI** - 现代、高性能的 Python Web 框架
- **Uvicorn** - ASGI 服务器

### 数据存储

- **JSON** - 轻量级数据存储（`backend/data/competitions.json`）

## 项目结构

```
.
├── frontend/                # 前端项目
│   ├── src/
│   │   ├── App.vue         # 主应用组件
│   │   ├── main.js         # 入口文件
│   │   └── components/
│   │       ├── CompetitionList.vue  # 竞赛列表组件
│   │       └── Guide.vue            # 竞赛指导组件
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── backend/                 # 后端项目
│   ├── app/
│   │   ├── main.py         # FastAPI 应用入口
│   │   ├── core/
│   │   │   └── config.py   # 配置文件
│   │   ├── api/
│   │   │   └── routes/
│   │   │       └── competitions.py  # 竞赛接口
│   │   └── schemas/
│   │       └── competition.py       # 数据模型
│   ├── data/
│   │   └── competitions.json        # 竞赛数据
│   └── requirements.txt
│
└── README.md
```

## 快速开始

### 环境要求

- Node.js 16+
- Python 3.9+

### 安装依赖

#### 前端

```bash
cd frontend
npm install
```

#### 后端

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 启动项目

#### 启动后端（端口 8000）

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### 启动前端（端口 3000）

```bash
cd frontend
npm run dev
```

### 访问应用

打开浏览器访问：http://localhost:3000

## API 接口

### 获取所有竞赛

```
GET /api/competitions
```

返回所有竞赛列表，按截止时间排序。

### 获取单个竞赛

```
GET /api/competitions/{id}
```

返回指定 ID 的竞赛详情。

## 数据说明

竞赛数据存储在 `backend/data/competitions.json`，包含以下字段：

- `id`: 竞赛唯一标识
- `name`: 竞赛名称
- `deadline`: 截止时间（ISO 8601 格式）
- `field`: 竞赛领域（如"算法/编程"、"综合/创新创业"）
- `difficulty`: 难度等级（简单/中等/困难）
- `level`: 竞赛级别（S/A+/A/B+/B）
- `description`: 竞赛简介
- `suggestions`: 参赛建议（数组）
- `links`: 相关链接（包含官网链接）

### 添加新竞赛

直接编辑 `backend/data/competitions.json`，按照现有格式添加新竞赛数据。后端会自动重载。

## 竞赛级别说明

- **S级**：国家级最高水平竞赛（如互联网+、挑战杯、ICPC）
- **A+级**：国家级重点竞赛
- **A级**：国家级竞赛
- **B+级**：省市级重点竞赛
- **B级**：省市级竞赛

## 设计理念

### UI 设计

- 简约风格：现代、注重细节
- 清晰的视觉层次和信息架构
- 流畅的交互动画和过渡效果
- 响应式设计，适配多种屏幕尺寸

### 功能设计

- 卡片式布局，信息一目了然
- 智能筛选和搜索，快速定位目标竞赛
- 详细的竞赛信息和参赛建议

## 后续优化方向

- [ ] 添加用户系统，支持个性化订阅
- [ ] 邮件/微信提醒功能
- [ ] 竞赛日历视图
- [ ] 数据来源标注与更新记录
- [ ] 自动爬取官方竞赛信息
- [ ] 移动端 App
- [ ] 竞赛标签系统
- [ ] 用户评论与经验分享

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎提交 Issue。

---

**注意**：竞赛截止时间请以官方公告为准，本系统仅供参考。
