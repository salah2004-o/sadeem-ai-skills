# 🤖 Sadeem AI Skills | نظام المهارات الذكية

> **Educational Framework for Building AI Agents with Skills, Registry, and Tool Management**  
> **إطار عمل تعليمي لبناء وكلاء ذكية مع أنظمة المهارات والسجلات وإدارة الأدوات**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Educational](https://img.shields.io/badge/Type-Educational-orange)]()

---

<div dir="ltr">

## 🌟 Overview

This is an **educational project** demonstrating how to build an AI Agent framework from scratch. It shows the core concepts of:

- **Agents** - Entry points that receive user commands
- **Skills** - Modular units that execute specific tasks
- **Skill Registry** - Central registry to manage and discover skills
- **Tools** - External APIs and services used by skills

### How It Works

```
User Input
    ↓
Agent (receives command)
    ↓
Skill Registry (finds matching skill)
    ↓
Skill Execution (runs the task)
    ↓
Output Result
```

---

## 🎯 Key Concepts

### 1. AI Agent
An AI Agent is a program that:
- Receives user requests
- Decides what to do
- Calls appropriate skills
- Returns results

### 2. Skill
A Skill is a modular execution unit with:
- `name` - Unique identifier
- `description` - What it does
- `execute()` - Implementation method

Example:
```python
class EchoSkill:
    name = "echo"
    description = "Echo the input text"
    
    def execute(self, input_text):
        return input_text
```

### 3. Skill Registry
A central registry that:
- Registers skills
- Retrieves skills by name
- Lists all available skills

### 4. Tools
External services or APIs that skills use:
- APIs
- Databases
- External services

---

## 📚 Architecture

```
sadeem-ai-skills/
├── agent.py              # Agent implementation
├── skill_registry.py     # Registry management
├── skills/
│   ├── echo_skill.py     # Example: Echo skill
│   ├── summarize_skill.py # Example: Summarize skill
│   └── ...
├── tools/
│   ├── api_client.py
│   └── ...
├── main.py              # Entry point
├── requirements.txt
├── ARCHITECTURE.md      # Technical docs
└── README.md
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/sadeem-ai-skills.git
cd sadeem-ai-skills

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the example
python main.py
```

---

## 💡 Example Usage

```python
from agent import Agent
from skill_registry import SkillRegistry
from skills.echo_skill import EchoSkill

# Create registry and register skills
registry = SkillRegistry()
registry.register(EchoSkill())

# Create agent with registry
agent = Agent(registry)

# Process user command
result = agent.process("/echo hello world")
# Output: "hello world"
```

---

## 🎓 Learning Objectives

This project teaches:
- ✅ How AI agents work
- ✅ Modular design patterns
- ✅ Registry patterns
- ✅ Skill composition
- ✅ Tool integration
- ✅ Software architecture basics

---

## 📝 License

MIT License

---

## 👤 Author

**Sadeem**

</div>

---

<div dir="rtl">

## 🌟 نظرة عامة

هذا **مشروع تعليمي** يوضح كيفية بناء إطار عمل وكيل ذكي من الصفر. يعرض المفاهيم الأساسية:

- **وكلاء** - نقاط دخول تستقبل أوامر المستخدم
- **مهارات** - وحدات معيارية تنفذ مهام محددة
- **سجل المهارات** - سجل مركزي لإدارة واكتشاف المهارات
- **أدوات** - واجهات برمجية وخدمات خارجية تستخدمها المهارات

### كيفية العمل

```
إدخال المستخدم
    ↓
الوكيل (استقبال الأمر)
    ↓
سجل المهارات (البحث عن المهارة المطابقة)
    ↓
تنفيذ المهارة (تشغيل المهمة)
    ↓
إخراج النتيجة
```

---

## 🎯 المفاهيم الأساسية

### 1. وكيل ذكي (AI Agent)
هو برنامج يقوم بـ:
- استقبال طلبات المستخدم
- تحديد ما يجب فعله
- استدعاء المهارات المناسبة
- إرجاع النتائج

### 2. مهارة (Skill)
وحدة تنفيذية معيارية تحتوي على:
- `name` - معرف فريد
- `description` - وصف الوظيفة
- `execute()` - طريقة التنفيذ

مثال:
```python
class EchoSkill:
    name = "echo"
    description = "عكس نص الإدخال"
    
    def execute(self, input_text):
        return input_text
```

### 3. سجل المهارات (Skill Registry)
سجل مركزي يقوم بـ:
- تسجيل المهارات
- استرجاع المهارات حسب الاسم
- إدراج جميع المهارات المتاحة

### 4. الأدوات (Tools)
خدمات أو واجهات برمجية خارجية:
- APIs
- قواعد البيانات
- الخدمات الخارجية

---

## 📚 البنية المعمارية

```
sadeem-ai-skills/
├── agent.py              # تطبيق الوكيل
├── skill_registry.py     # إدارة السجل
├── skills/
│   ├── echo_skill.py     # مثال: مهارة echo
│   ├── summarize_skill.py # مثال: مهارة الملخص
│   └── ...
├── tools/
│   ├── api_client.py
│   └── ...
├── main.py              # نقطة الدخول
├── requirements.txt
├── ARCHITECTURE.md      # الوثائق الهندسية
└── README.md
```

---

## 🚀 البدء السريع

```bash
# استنساخ المستودع
git clone https://github.com/your-username/sadeem-ai-skills.git
cd sadeem-ai-skills

# إنشاء بيئة افتراضية
python -m venv venv
venv\Scripts\activate

# تثبيت المتطلبات
pip install -r requirements.txt

# تشغيل المثال
python main.py
```

---

## 💡 مثال على الاستخدام

```python
from agent import Agent
from skill_registry import SkillRegistry
from skills.echo_skill import EchoSkill

# إنشاء السجل وتسجيل المهارات
registry = SkillRegistry()
registry.register(EchoSkill())

# إنشاء الوكيل مع السجل
agent = Agent(registry)

# معالجة أمر المستخدم
result = agent.process("/echo hello world")
# النتيجة: "hello world"
```

---

## 🎓 أهداف التعلم

هذا المشروع يعلم:
- ✅ كيفية عمل وكلاء ذكية
- ✅ أنماط التصميم المعياري
- ✅ أنماط السجل
- ✅ تركيب المهارات
- ✅ تكامل الأدوات
- ✅ أساسيات معمارية البرمجيات

---

## 📝 الترخيص

MIT License

---

## 👤 المؤلف

**Sadeem | صديم**

</div>

---

**Last Updated**: 2026-09-01
**آخر تحديث**: 2026-09-01


- من يقرر ماذا يطلب المستخدم؟ → الـAgent
- من يحتوي المهارات؟ → Skill Registry
- من ينفذ المهمة؟ → Skill

## 4) الفرق بين Skill وTool

### Skill
Skill هي المهمة نفسها أو الوظيفة المعرفية.

مثال:

- `summarize`
- `echo`

### Tool
Tool هو أداة أو خدمة تستخدمها الـSkill لتنفيذ المهمة.

مثال:

- `Gemini API`
- دالة تنظيف النص
- خدمة خارجية أخرى

باختصار:

- Skill = القرار/المهمة
- Tool = التنفيذ الحقيقي أو الخدمة الخارجية

## 5) كيف يمر الطلب داخل النظام

عند كتابة أمر مثل:

```text
YOU: /echo hello
```

يتم التدفق كالتالي:

```text
User
 ↓
Agent
 ↓
Skill Registry
 ↓
EchoSkill
 ↓
Result
 ↓
User
```

وعند الأمر:

```text
YOU: /summarize Python is a programming language...
```

يكون التدفق:

```text
User
 ↓
Agent
 ↓
Skill Registry
 ↓
SummarizeSkill
 ↓
Gemini API
 ↓
Result
 ↓
User
```

## 6) كيف أضيف Skill جديدة

لإضافة Skill جديد، اتبع الخطوات التالية:

1. أنشئ مجلدًا داخل `app/skills/`
2. أضف ملف `skill.py`
3. ورث من `Skill`
4. حدد `name` و `description`
5. نفذ `execute()`
6. سجل المهارة داخل `app/agent/registry.py`

مثال بسيط:

```python
from app.skills import Skill


class WeatherSkill(Skill):
    name = "weather"
    description = "Gets the weather for a city"

    def execute(self, text: str) -> str:
        return f"Weather for: {text}"
```

ثم في الـRegistry:

```python
registry.register(WeatherSkill())
```

## 7) كيف أشغل المشروع

### التثبيت

```bash
cd sadeem-ai-skills
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### التشغيل

```bash
python -m app.main
```

## 8) كيف أضع Gemini API Key

أنشئ ملف `.env` من ملف المثال:

```bash
copy .env.example .env
```

ثم عدّل القيم:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

تأكد أن الملف `.env` غير مضاف إلى Git لأنه موجود في `.gitignore`.

## 9) أمثلة تشغيل

### مثال 1: echo

```text
Sadeem AI Agent

YOU: skills
Available skills:
- echo
- summarize

YOU: /echo hello
AGENT: hello
```

### مثال 2: summarize

```text
YOU: /summarize Python is a programming language used for web apps, automation, and data analysis.
AGENT: Python is a general-purpose programming language ...
```

إذا لم يتم ضبط مفتاح Gemini، فسيعود رسالة واضحة بدل أن يتوقف التطبيق.

## المرحلة الثانية (لن تنفذ الآن)

المرحلة الحالية تعتمد على `Manual Router` فقط، أي أن الـAgent يختار المهارة يدويًا بناءً على اسم الأمر.

لكن لاحقًا يمكن تطوير النظام إلى بنية أكثر ذكاءً:

```text
User
 ↓
LLM Agent
 ↓
Skill Selection
 ↓
Permission Check
 ↓
Skill
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
User
```

في هذه المرحلة، لا نضيف LLM لاختيار المهارة، ولا نضيف صلاحيات، ولا قواعد بيانات. 
الهدف الآن هو فهم البنية الأساسية فقط.

## المشروع الحالي

هذا المشروع يركز على:

- الفهم البصري للهيكل
- فصل المهام بين Agent وSkill وTool
- فهم دور Registry
- تعليمية ومباشرة قبل إدخال تعقيد إضافي

## ملاحظات بسيطة

- لا تستخدم LangChain أو LangGraph أو CrewAI في هذه المرحلة.
- لا تضع API key داخل الكود.
- كل ملف صغير وواضح.
- الهدف هو القراءة والتنقل داخل المشروع لفهم العلاقة بين الملفات.
