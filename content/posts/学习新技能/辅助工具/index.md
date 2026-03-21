+++
date = '2026-03-04T09:18:29+08:00'
draft = false
title = '辅助工具'
categories = ["学习新技能"]
+++



# 三件套使用说明：Watt Toolkit + Clash Verge + Obsidian

## 1. Clash Verge（全局代理 / 梯子）

**核心定位**：日常科学上网工具，支持代理模式与 TUN 模式，用于访问 GitHub、部署博客等场景。

### 主要功能

- **代理模式**：浏览器 / 应用通过代理端口访问网络，适合需要精细控制代理范围的场景。
- **TUN 模式**：将系统流量全部接管，实现全局代理，适合需要无差别访问外网的场景。
- **规则管理**：可自定义分流规则，自动区分国内外网站，避免不必要的代理。

### 使用步骤

1. **启动与配置**
    
    - 双击桌面图标打开 Clash Verge，确保配置文件已导入（`.yaml` 或 `.yml`）。
    - 在「设置」中开启「系统代理」或「TUN 模式」（二选一，TUN 模式覆盖范围更广）。
    
2. **验证连接**
    
    - 打开浏览器访问 `https://ipinfo.io`，查看 IP 地址是否已切换到代理节点。
    - 若访问 GitHub 等网站正常，说明代理生效。
    
3. **注意事项**
    
    - 开启 TUN 模式后，部分本地服务（如 `localhost`）可能受影响，可在规则中添加例外。
    - 关闭 Clash Verge 前，先关闭系统代理，避免网络异常。
    

---

## 2. Watt Toolkit（GitHub 专用加速器）

**核心定位**：当 Clash Verge 不可用时，用于加速 GitHub 访问、克隆 / 推送代码等操作。

### 主要功能

- **GitHub 加速**：优化 GitHub 域名解析，提升访问速度，支持 Git 操作加速。
- **多平台支持**：可同时加速 GitHub、GitLab 等代码托管平台。
- **无需全局代理**：仅针对指定平台生效，不影响其他网络访问。

### 使用步骤

1. **启动与加速**
    
    - 打开 Watt Toolkit，在「加速列表」中勾选「GitHub」。
    - 点击「一键加速」，等待提示「加速成功」。
    
2. **验证效果**
    
    - 在 CMD 中执行 `git clone` 或 `git push`，观察速度是否提升。
    - 若 Clash Verge 未开启，Watt Toolkit 可作为备用方案。
    
3. **注意事项**
    
    - 仅在需要访问 GitHub 时开启，无需长期后台运行。
    - 若同时开启 Clash Verge，可能产生冲突，建议优先使用 Clash Verge，仅在其失效时切换到 Watt Toolkit。
    

---

## 3. Obsidian（Markdown 博客编辑器）

**核心定位**：本地 Markdown 写作工具，用于编写 Hugo 博客文章，支持双链笔记、实时预览等功能。

### 主要功能

- **Markdown 编辑**：支持标准 Markdown 语法，实时预览排版效果。
- **本地库管理**：将博客文章以文件夹形式组织，便于版本控制。
- **插件生态**：可安装「Git 集成」「模板」等插件，简化博客发布流程。

### 使用步骤

1. **创建博客库**
    
    - 打开 Obsidian，选择「打开文件夹作为库」，指向 Hugo 站点的 `content/posts` 目录（所有博客文章存放于此）。
    - 新建 `.md` 文件，文件名即为文章 URL（如 `my-first-post.md`）。
    
2. **编写与预览**
    
    - 在编辑器中编写内容，使用 `---` 分隔 Front Matter（文章元数据）：
        
        markdown
        
        ```
        ---
        title: "我的第一篇博客"
        date: 2026-03-04T12:00:00+08:00
        categories: ["技术"]
        tags: ["Hugo", "Obsidian"]
        ---
        正文内容...
        ```
        
    - 点击「预览」按钮，查看文章在 Hugo 中的渲染效果。
    
3. **发布流程**
    
    - 文章完成后，在 Obsidian 中使用 Git 插件提交修改，或手动在 CMD 中执行：
        
        bash
        
        运行
        
        ```
        cd D:\blog\andrea
        git add content/posts/
        git commit -m "新增文章：我的第一篇博客"
        git push origin main
        ```
        
    - 再通过 `hugo` 构建静态文件，部署到 GitHub Pages。
    

---

## 三件套配合使用流程

1. **日常写作**：
    
    - 打开 Obsidian，在 `content/posts` 中编写文章。
    - 开启 Clash Verge（TUN 模式），确保能正常访问 GitHub。
    
2. **部署博客**：
    
    - 在 Hugo 根目录执行 `hugo` 生成 `public` 文件夹。
    - 进入 `public` 目录，通过 Git 推送到 `gh-pages` 分支。
    
3. **应急场景**：
    - 若 Clash Verge 失效，关闭系统代理，打开 Watt Toolkit 加速 GitHub，完成 Git 操作后再关闭。