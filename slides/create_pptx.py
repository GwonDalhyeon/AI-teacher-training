#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates ChatGPT를_이용한_수업_조언자_만들기.pptx
Template: source/template_unpacked  |  Content: PPT_원고.md
"""
import re, shutil, html, sys
from pathlib import Path

TEMPLATE = Path(r"D:\Projects\AI-teacher-training\source\template_unpacked")
WORK     = Path(r"D:\Projects\AI-teacher-training\slides\work_unpacked")
SKILLS   = Path(r"C:\Users\권달현\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\d7fd726a-bab2-4816-8437-3b0b64373665\9f078a52-adb3-4390-8b8e-fb3d56194039\skills\pptx")
OUTPUT   = Path(r"D:\Projects\AI-teacher-training\slides\ChatGPT를_이용한_수업_조언자_만들기.pptx")
sys.path.insert(0, str(SKILLS / "scripts"))

def e(t): return html.escape(str(t or ""), quote=False)

# ─── XML primitives ────────────────────────────────────────────────────────────

SLD_HEAD = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">\n'
            '  <p:cSld>\n    <p:spTree>\n'
            '      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>\n'
            '      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
            '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>\n')
SLD_TAIL = ('    </p:spTree>\n  </p:cSld>\n'
            '  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>\n</p:sld>')

def para(text="", nobullet=False, bold=False, red=False, sz=None, align=None):
    pPr = ""
    if nobullet:
        pPr = '<a:pPr marL="0" indent="0">'
        if align:
            pPr = f'<a:pPr marL="0" indent="0" algn="{align}">'
        pPr += "<a:buNone/></a:pPr>"
    elif align:
        pPr = f'<a:pPr algn="{align}"/>'
    if not text:
        return f"<a:p>{pPr}<a:endParaRPr lang=\"ko-KR\" dirty=\"0\"/></a:p>"
    attrs = 'lang="ko-KR" dirty="0"'
    if bold: attrs += ' b="1"'
    if sz:   attrs += f' sz="{sz}"'
    fill = '<a:solidFill><a:srgbClr val="FF0000"/></a:solidFill>' if red else ""
    return f"<a:p>{pPr}<a:r><a:rPr {attrs}>{fill}</a:rPr><a:t>{e(text)}</a:t></a:r></a:p>"

def title_sp(text, ph_type="title", idx=None):
    idx_attr = f' idx="{idx}"' if idx is not None else ""
    return (f'      <p:sp>\n'
            f'        <p:nvSpPr><p:cNvPr id="2" name="제목 1"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr><p:ph type="{ph_type}"{idx_attr}/></p:nvPr></p:nvSpPr>\n'
            f'        <p:spPr/>\n'
            f'        <p:txBody><a:bodyPr/><a:lstStyle/>'
            f'<a:p><a:r><a:rPr lang="ko-KR" dirty="0"/><a:t>{e(text)}</a:t></a:r></a:p>'
            f'</p:txBody>\n      </p:sp>\n')

def content_sp(items, idx=1, id_num=3, half=False):
    half_attr = ' sz="half"' if half else ""
    body = "".join(para(**item) if isinstance(item, dict) else para(item) for item in items)
    return (f'      <p:sp>\n'
            f'        <p:nvSpPr><p:cNvPr id="{id_num}" name="내용 {id_num-1}"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr><p:ph{half_attr} idx="{idx}"/></p:nvPr></p:nvSpPr>\n'
            f'        <p:spPr/>\n'
            f'        <p:txBody><a:bodyPr/><a:lstStyle/>{body}</p:txBody>\n'
            f'      </p:sp>\n')

def textbox_sp(lines, x, y, cx, cy, sz=2800, bold=False, align="ctr", id_num=4):
    bold_a = ' b="1"' if bold else ""
    paras = "".join(
        f'<a:p><a:pPr algn="{align}"><a:buNone/></a:pPr>'
        f'<a:r><a:rPr lang="ko-KR" dirty="0" sz="{sz}"{bold_a}/>'
        f'<a:t>{e(ln)}</a:t></a:r></a:p>'
        for ln in (lines if isinstance(lines, list) else lines.split("\n"))
    )
    return (f'      <p:sp>\n'
            f'        <p:nvSpPr><p:cNvPr id="{id_num}" name="텍스트상자 {id_num}"/>'
            f'<p:cNvSpPr txBox="1"><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr/></p:nvSpPr>\n'
            f'        <p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/>'
            f'</a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
            f'<a:noFill/></p:spPr>\n'
            f'        <p:txBody><a:bodyPr wrap="square" rtlCol="0"/>'
            f'<a:lstStyle/>{paras}</p:txBody>\n      </p:sp>\n')

def table_sp(headers, rows, x=457200, y=1300000):
    W, H_TOTAL = 11277600, 6858000 - y - 150000
    nc = len(headers)
    nr = len(rows) + 1
    cw = W // nc
    rh = H_TOTAL // nr
    def cell(txt, bold=False):
        ba = " b=\"1\"" if bold else ""
        return (f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>'
                f'<a:p><a:pPr algn="ctr"/>'
                f'<a:r><a:rPr lang="ko-KR" dirty="0"{ba}/>'
                f'<a:t>{e(txt)}</a:t></a:r></a:p>'
                f'</a:txBody><a:tcPr/></a:tc>')
    hdr_row = f'<a:tr h="{rh}">{"".join(cell(h, True) for h in headers)}</a:tr>'
    data_rows = "".join(
        f'<a:tr h="{rh}">{"".join(cell(c) for c in row)}</a:tr>'
        for row in rows
    )
    grid = "".join(f'<a:gridCol w="{cw}"/>' for _ in headers)
    return (f'      <p:graphicFrame>\n'
            f'        <p:nvGraphicFramePr>'
            f'<p:cNvPr id="4" name="표 3"/>'
            f'<p:cNvGraphicFramePr><a:graphicFrameLocks noGrp="1"/></p:cNvGraphicFramePr>'
            f'<p:nvPr/></p:nvGraphicFramePr>\n'
            f'        <p:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{W}" cy="{H_TOTAL}"/></p:xfrm>\n'
            f'        <a:graphic><a:graphicData '
            f'uri="http://schemas.openxmlformats.org/drawingml/2006/table">\n'
            f'          <a:tbl>\n'
            f'            <a:tblPr firstRow="1">'
            f'<a:tableStyleId>{{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}}</a:tableStyleId>'
            f'</a:tblPr>\n'
            f'            <a:tblGrid>{grid}</a:tblGrid>\n'
            f'            {hdr_row}\n            {data_rows}\n'
            f'          </a:tbl>\n'
            f'        </a:graphicData></a:graphic>\n'
            f'      </p:graphicFrame>\n')

# ─── Slide generators ──────────────────────────────────────────────────────────

def slide_title(d):
    xml = SLD_HEAD
    xml += title_sp(d["center_title"], ph_type="ctrTitle")
    subs = [para(ln) for ln in d["subtitle"]]
    xml += (f'      <p:sp>\n'
            f'        <p:nvSpPr><p:cNvPr id="3" name="부제목 2"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr><p:ph type="subTitle" idx="1"/></p:nvPr></p:nvSpPr>\n'
            f'        <p:spPr/>\n'
            f'        <p:txBody><a:bodyPr/><a:lstStyle/>{"".join(subs)}</p:txBody>\n'
            f'      </p:sp>\n')
    return xml + SLD_TAIL

def slide_content(d):
    xml = SLD_HEAD + title_sp(d["title"]) + content_sp(d["items"])
    return xml + SLD_TAIL

def slide_large(d):
    xml = SLD_HEAD + title_sp(d["title"])
    main_sz = d.get("main_sz", 5400)
    xml += textbox_sp(d["main_text"], 457200, 1400000, 11277600, 3000000,
                      sz=main_sz, bold=True, align="ctr", id_num=4)
    if d.get("sub_text"):
        xml += textbox_sp(d["sub_text"], 457200, 4600000, 11277600, 1700000,
                          sz=2000, bold=False, align="ctr", id_num=5)
    return xml + SLD_TAIL

def slide_table(d):
    xml = SLD_HEAD + title_sp(d["title"]) + table_sp(d["headers"], d["rows"])
    return xml + SLD_TAIL

def slide_twocol(d):
    xml = SLD_HEAD + title_sp(d["title"])
    left = [{"text": d.get("left_title",""), "bold": True, "nobullet": True},
            {"text": "", "nobullet": True}]
    left += [{"text": t} for t in d["left_items"]]
    right = [{"text": d.get("right_title",""), "bold": True, "nobullet": True},
             {"text": "", "nobullet": True}]
    right += [{"text": t} for t in d["right_items"]]
    xml += content_sp(left,  idx=1, id_num=3, half=True)
    xml += content_sp(right, idx=2, id_num=4, half=True)
    return xml + SLD_TAIL

def slide_demo(d):
    items = [{"text": d["url"], "sz": 2400, "bold": True, "nobullet": True},
             {"text": "", "nobullet": True}]
    for ln in d["key_point"].split("\n"):
        items.append({"text": ln, "nobullet": True})
    xml = SLD_HEAD + title_sp(d["title"]) + content_sp(items)
    return xml + SLD_TAIL

GENERATORS = {
    "title":    (slide_title,   "slideLayout1.xml"),
    "content":  (slide_content, "slideLayout2.xml"),
    "large":    (slide_large,   "slideLayout11.xml"),
    "table":    (slide_table,   "slideLayout2.xml"),
    "twocol":   (slide_twocol,  "slideLayout9.xml"),
    "demo":     (slide_demo,    "slideLayout2.xml"),
}

# ─── Slide definitions (38 slides) ────────────────────────────────────────────

SLIDES = [
# S01
{"type":"title","center_title":"ChatGPT를 이용한 수업 조언자 만들기",
 "subtitle":["나만의 AI 수업 파트너 설정하기","권달현"],
 "notes":"(오프닝, 자기소개)"},

# S02
{"type":"content","title":"오늘 하루 연수 구조",
 "items":[
  {"text":"[앞 강의 3h]  AI 활용 개론","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"[이 강의 3h]  수업 조언자 만들기  ← 지금 여기","nobullet":True,"bold":True},
  {"text":"","nobullet":True},
  {"text":"[뒤 강의 6h]  AI 수업 준비·활용","nobullet":True},
 ],
 "notes":"오늘 하루는 12시간 연수입니다. 앞에서는 AI 전반을 다뤘고, 뒤에서는 AI를 수업에 직접 쓰는 방법을 다룹니다. 제 시간은 그 사이 다리 역할입니다."},

# S03
{"type":"large","title":"이 3시간이 끝날 때",
 "main_text":"내 수업 조언자가\n실제로 작동하는 상태",
 "sub_text":"뒤 강의는 이 조언자가 있다는 전제로 시작합니다",
 "notes":"오늘 만들어두지 않으면 뒤 강의에서 출발선이 달라집니다. 오늘 하나만 가져가신다면, 살아있는 조언자 프로젝트입니다."},

# S04
{"type":"content","title":"오늘 흐름",
 "items":[
  {"text":"1. 수업 조언자가 뭔가요?"},
  {"text":"2. 어떤 AI를 쓸까요?"},
  {"text":"3. 내 조언자 만들기  ← 핵심","bold":True},
  {"text":"4. 조언자 써보기"},
  {"text":"5. AI로 수업 도구 만들기"},
 ],
 "notes":"순서대로 진행합니다. 3번이 가장 중요하고 가장 시간이 길어요."},

# S05
{"type":"large","title":"지금까지 AI를 어떻게 쓰셨나요?",
 "main_sz":4000,
 "main_text":"지금까지 AI와 대화할 때\n어떤 점이 불편하셨나요?",
 "sub_text":"잠깐 생각해보세요. 옆 분과 한 마디씩만 나눠봐도 좋습니다.",
 "notes":"잠깐 생각해보세요. 옆 분과 한 마디씩만 나눠봐도 좋습니다."},

# S06
{"type":"table","title":"일반 AI 채팅의 한계",
 "headers":["일반 AI 채팅","수업 조언자 프로젝트"],
 "rows":[
  ["매번 새로 설명","한 번 설정하면 유지"],
  ["무엇이든 대답하려 함","설계된 원칙대로 작동"],
  ["창 닫으면 사라짐","프로젝트 안에 축적"],
  ["반영 안 됨","처음부터 알고 있음"],
 ],
 "notes":"이 차이가 바로 오늘 하는 것의 이유입니다."},

# S07
{"type":"content","title":"ChatGPT 프로젝트 기능이란?",
 "items":[
  {"text":"프로젝트 = 하나의 작업 공간","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"안에 넣어둔 것들:","nobullet":True},
  {"text":"지침 (행동 원칙)"},
  {"text":"파일 (내 맥락 정보)"},
  {"text":"대화 내역"},
  {"text":"","nobullet":True},
  {"text":"→ 모든 대화에 자동 적용","bold":True,"nobullet":True},
 ],
 "notes":"프로젝트는 하나의 작업 공간입니다. 안에 넣어둔 지침과 파일이 모든 대화에 자동으로 반영됩니다."},

# S08
{"type":"content","title":"Layer 1 — 조언자의 행동 원칙",
 "items":[
  {"text":"이미 완성됨. 오늘 붙여넣기만 하면 됩니다.","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"원칙 예시:","nobullet":True},
  {"text":"교사의 판단을 대체하지 않고 질문·보완·점검"},
  {"text":"기준 문서를 수호"},
  {"text":"한 번에 2~3개 논점만 다룸"},
 ],
 "notes":"이 문서가 조언자의 성격을 결정합니다. 여러분이 직접 작성하실 필요 없고, 오늘 제공된 파일을 그대로 쓰시면 됩니다."},

# S09
{"type":"content","title":"Layer 2 — 내 맥락 계약",
 "items":[
  {"text":"오늘 함께 만드는 것","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"1. 역할 설정 (내 수업 철학, 기대하는 역할)"},
  {"text":"2. 교사 프로필 (교과, 학교급·학년)"},
  {"text":"3. 학급 맥락 (학생 특성)"},
  {"text":"4. 운영 여건 (시수, 환경)"},
  {"text":"5. 기준 문서 (교육과정, 성취기준 등)"},
 ],
 "notes":"오늘 조언자와 대화를 나누면서 이 다섯 가지를 채웁니다. 조언자가 먼저 질문을 합니다."},

# S10
{"type":"table","title":"어떤 AI든 같은 구조로 설정할 수 있습니다",
 "headers":["ChatGPT 프로젝트","Gemini Gems","Claude Projects"],
 "rows":[
  ["OpenAI 제작","Google 제작","Anthropic 제작"],
  ["프로젝트 기능","Gems 기능","Projects 기능"],
  ["오늘 기준 플랫폼","한도 초과 시 대체","참고용"],
 ],
 "notes":"오늘은 ChatGPT 기준으로 진행합니다. 다른 AI를 쓰시는 분은 같은 구조를 그 AI에 적용하시면 됩니다."},

# S11
{"type":"content","title":"오늘 사용하는 파일",
 "items":[
  {"text":"두 파일 모두 제공됩니다","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"[지침에 붙여넣기]","bold":True,"nobullet":True},
  {"text":"ChatGPT용_수업설계조언자_프로젝트지침","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"[소스로 업로드]","bold":True,"nobullet":True},
  {"text":"Layer_2_수업설계조언자","nobullet":True},
 ],
 "notes":"이 두 파일이 오늘 핵심 재료입니다. 파일명을 기억해두세요."},

# S12
{"type":"content","title":"ChatGPT 한도가 차면?",
 "items":[
  {"text":"한도 초과 알림","nobullet":True},
  {"text":"→  Gemini 접속","nobullet":True},
  {"text":"→  Gems 만들기","nobullet":True},
  {"text":"→  Gems용 지침 붙여넣기","nobullet":True},
  {"text":"→  Layer 2 파일 업로드","nobullet":True},
  {"text":"→  ChatGPT 대화 내용 복사·붙여넣기","nobullet":True},
  {"text":"→  이어서 진행","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"연수자 자료 '무료 한도 초과 시' 항목 참고","nobullet":True},
 ],
 "notes":"무료 계정은 꽤 빨리 한도가 차기도 합니다. 걱정하지 마세요. Gemini로 넘어가면 동일하게 진행하실 수 있습니다."},

# S13
{"type":"content","title":"먼저 3분, 준비 카드 작성",
 "items":[
  {"text":"연수자 자료 3쪽 참고","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"교과:"},
  {"text":"학교급·학년:"},
  {"text":"자주 하는 수업 관련 작업:"},
  {"text":"AI에게 도움받고 싶은 것:"},
  {"text":"AI가 하지 않았으면 하는 것:"},
 ],
 "notes":"본격적으로 시작하기 전에 3~5분만 이 카드를 작성해주세요. Layer 2 대화를 시작할 때 이 내용이 도움이 됩니다."},

# S14
{"type":"content","title":"1단계 — ChatGPT 프로젝트 만들기",
 "items":[
  {"text":"chatgpt.com → 왼쪽 메뉴 → 프로젝트 → 새 프로젝트","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"이름 예시:","bold":True,"nobullet":True},
  {"text":"수업 설계 조언자"},
  {"text":"○○교과 수업 조언자"},
 ],
 "notes":"chatgpt.com 접속하시고, 왼쪽 메뉴에서 '프로젝트'를 찾아주세요. 없으면 스크롤을 내려보세요."},

# S15
{"type":"content","title":"2단계 — Layer 1 프로젝트 지침 붙여넣기",
 "items":[
  {"text":"프로젝트 설정 → 지침 칸","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"ChatGPT용_수업설계조언자_프로젝트지침 파일 전체 복사 → 붙여넣기","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"Ctrl+A → Ctrl+C → 지침 칸에 Ctrl+V","nobullet":True},
 ],
 "notes":"파일을 열어서 전체 선택(Ctrl+A), 복사(Ctrl+C), 지침 칸에 붙여넣기(Ctrl+V)하시면 됩니다."},

# S16
{"type":"content","title":"3단계 — Layer 2 파일 업로드",
 "items":[
  {"text":"파일 추가 / 소스 추가 버튼 클릭","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"Layer_2_수업설계조언자 파일 업로드","bold":True,"nobullet":True},
 ],
 "notes":"'파일 추가' 또는 '소스 추가'를 클릭하고 Layer 2 파일을 업로드합니다."},

# S17
{"type":"content","title":"4단계 — 첫 대화 시작",
 "items":[
  {"text":"프로젝트 안에서 새 채팅 시작","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"첫 메시지 예시:","bold":True,"nobullet":True},
  {"text":'"안녕하세요. Layer 2를 구성하고 싶습니다."',"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"조언자가 먼저 질문을 시작합니다 → 대화로 진행","nobullet":True},
 ],
 "notes":"조언자가 먼저 질문을 시작할 거예요. 질문에 답하는 방식으로 진행하시면 됩니다. 준비 카드를 옆에 두고 참고하세요."},

# S18
{"type":"content","title":"Layer 2 구성 중 — 이런 질문을 받게 됩니다",
 "items":[
  {"text":'"어떤 교과를 담당하고 계신가요?"'},
  {"text":'"AI 조언자에게 어떤 역할을 기대하시나요?"'},
  {"text":'"평소 수업에서 어떤 점이 가장 어렵게 느껴지시나요?"'},
  {"text":'"수업 철학이나 지향하는 방향이 있으신가요?"'},
  {"text":"","nobullet":True},
  {"text":"Tip: 모르겠으면 솔직하게 모르겠다고 해도 됩니다","nobullet":True},
 ],
 "notes":"조언자가 이런 질문들을 순서대로 할 거예요. 준비 카드 내용을 바탕으로 자연스럽게 답하시면 됩니다. (이 슬라이드는 진행 중 참고용으로 남겨둡니다)"},

# S19
{"type":"content","title":"이제 써봅시다",
 "items":[
  {"text":"내 실제 수업 고민을 넣어보세요","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"질문 유형 4가지:","nobullet":True},
  {"text":"수업 설계 피드백"},
  {"text":"활동 아이디어"},
  {"text":"목표-활동-평가 점검"},
  {"text":"자료 초안 요청"},
 ],
 "notes":"Layer 2가 어느 정도 채워졌으면, 지금 실제로 수업에서 고민하고 있는 것을 질문해보세요."},

# S20
{"type":"content","title":"어떻게 나왔나요?",
 "items":[
  {"text":'"2~3분, 화면 공유해주실 분 계신가요?"',"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"확인 포인트:","nobullet":True},
  {"text":"내 교과·학급이 반영되었는가?"},
  {"text":"단순 아이디어 나열이 아닌가?"},
  {"text":"내 수업 철학과 다를 때 명시적으로 알려주었는가?"},
 ],
 "notes":"결과를 공유하고 싶으신 분은 화면을 보여주세요. 잘 나온 것도, 이상하게 나온 것도 다 좋습니다."},

# S21
{"type":"content","title":"Layer 2가 쌓일수록 달라집니다",
 "items":[
  {"text":"오늘은 시작입니다","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"처음 만난 동료  vs  1년 같이 일한 동료","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"대화를 계속 이어갈수록","nobullet":True},
  {"text":"조언자는 여러분을 더 잘 알게 됩니다","nobullet":True},
 ],
 "notes":"오늘 Layer 2가 완성되지 않아도 괜찮습니다. 이후 대화를 거치며 계속 채워집니다."},

# S22
{"type":"twocol","title":"AI를 쓰는 두 가지 방식",
 "left_title":"웹 기반 AI",
 "left_items":["브라우저에서 접속","설치 없음","결과를 복사해서 씀","→ 오늘 사용한 방식"],
 "right_title":"로컬 설치 AI",
 "right_items":["터미널에서 실행","내 컴퓨터에 직접 설치","파일을 직접 생성·수정","→ 또 다른 방식"],
 "notes":"지금까지는 웹 기반 AI를 썼습니다. 또 다른 방식이 있어요."},

# S23
{"type":"twocol","title":"로컬 설치 AI — Claude Code와 Codex",
 "left_title":"Claude Code",
 "left_items":["Anthropic 제작","터미널에서 claude 명령어","말로 요청 → 파일 자동 생성"],
 "right_title":"Codex",
 "right_items":["OpenAI 제작","터미널에서 codex 명령어","말로 요청 → 파일 자동 생성"],
 "notes":"제가 오늘 보여드릴 웹앱들은 이 도구를 써서 만들었습니다. 말로 요청하면 파일이 컴퓨터에 직접 생겨요."},

# S24
{"type":"large","title":"로컬 설치 AI, 지금 당장 써야 할까요?",
 "main_sz":7200,
 "main_text":"아니요.",
 "sub_text":"오늘은 '이런 것도 있다'를 알면 충분합니다.\n관심 있는 분은 이후에 도전해볼 수 있는 영역입니다.",
 "notes":"설치 과정이 있고 터미널을 써야 해서 처음엔 낯설 수 있어요. 오늘 실습은 웹 기반으로 합니다."},

# S25
{"type":"content","title":"수업 도구 웹앱이 필요한 순간",
 "items":[
  {"text":"두 조건이 겹칠 때:","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"1. 학생들이 잘못된 직관을 갖고 있을 때"},
  {"text":"2. 설명이나 숫자만으로는 그 직관이 잘 바뀌지 않을 때"},
  {"text":"","nobullet":True},
  {"text":"움직이는 시뮬레이션이 정지된 설명보다 강할 때","bold":True,"nobullet":True},
 ],
 "notes":"AI로 도구를 만드는 것 자체가 목적이 아닙니다. 수업에서 꼭 필요한 순간에 써야 의미가 있어요."},

# S26
{"type":"large","title":"수학 수업 사례 — 질문 하나",
 "main_sz":3600,
 "main_text":'"참석 확률이 70%니까\n70%만 준비하면 충분하지 않나요?"',
 "sub_text":"확률과 통계 수업에서 학생들이 갖고 오는 직관",
 "notes":"여러분은 어떻게 생각하세요? 잠깐 생각해보세요."},

# S27
{"type":"large","title":"실제로는?",
 "main_sz":9600,
 "main_text":"41.6%",
 "sub_text":"기댓값만큼 준비하면 10번 중 4번은 준비가 부족합니다\n이 사실을 말로 설명할 수 있지만, 직접 경험하는 것은 다릅니다",
 "notes":"70%만 준비하면 40%가 넘는 확률로 부족해요. 왜 그럴까요? (잠깐 받기) 이걸 학생들이 직접 경험하게 만드는 것이 오늘 보여드릴 웹앱입니다."},

# S28
{"type":"demo","title":"[시연] 표본비율과 행사 준비 실험실",
 "url":"gwondalhyeon.github.io/AI-teacher-training/webapps/sample-ratio-lab/",
 "key_point":"슬라이더 3개: 신청자 수 / 참석 확률 / 여유 준비 비율\n기본값 n=20, p=0.7 → 준비 부족 확률 41.6%\nn을 100으로 올리면 → 큰 수의 법칙",
 "notes":"슬라이더 세 개입니다. 신청자 수, 참석 확률, 여유 준비 비율.\n기본값은 n=20, p=0.7, r=0, 즉 70%만 준비.\n준비 부족 확률이 41.6%로 표시됩니다.\n자동 실행을 눌러볼게요. 빨간 막대가 계속 나오죠?\n이제 r을 조금 올려봅니다. 10% 더 준비하면 10.7%로 줄어요.\nn을 100으로 올리면요? 신기하게도 같은 비율(80%)로 준비해도 더 안정적입니다.\n이게 큰 수의 법칙입니다."},

# S29
{"type":"content","title":"이 수업의 설계 흐름",
 "items":[
  {"text":"학생 직관 확인","nobullet":True},
  {"text":"→  앱으로 직관 충돌 경험","nobullet":True},
  {"text":"→  학습지로 수치 확인","nobullet":True},
  {"text":"→  여유 비율 조절 실험","nobullet":True},
  {"text":"→  의사결정 토론","nobullet":True},
  {"text":"","nobullet":True},
  {"text":"앱은 수업 시퀀스의 한 부분","bold":True,"nobullet":True},
 ],
 "notes":"앱이 전부가 아니에요. 학습지와 토론이 함께 있어야 수업이 됩니다. AI로 만든 웹앱이 이 흐름의 어디에 들어가는지가 중요합니다."},

# S30
{"type":"content","title":"여러분 교과에서 찾아보기",
 "items":[
  {"text":'"우리 학생들이 잘못된 직관을 갖고 오는 개념이 있나요?"',"nobullet":True},
  {"text":"","nobullet":True},
  {"text":'"그 직관을 깨는 데 움직이는 시뮬레이션이 효과적일까요?"',"nobullet":True},
 ],
 "notes":"잠깐 생각해보시고, 생각이 떠오른 분은 말씀해주세요."},

# S31
{"type":"content","title":"교과별 웹앱 갤러리",
 "items":[
  {"text":"gwondalhyeon.github.io/AI-teacher-training/webapps/","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"자연과학 계열: 움직임, 방향, 변화율"},
  {"text":"사회·법 계열: 이해관계, 우선순위, 조건부 판단"},
  {"text":"","nobullet":True},
  {"text":"공통 구조: 깨야 할 직관 → 조작 → 눈에 보이는 변화","nobullet":True},
 ],
 "notes":"이 목록은 웹앱 자랑 목록이 아니라 수업 설계 예시입니다.\n교과가 달라도 구조는 같습니다.\n학생이 갖고 오는 직관이 있고, 그 직관을 조작과 변화로 흔드는 겁니다."},

# S32
{"type":"demo","title":"[대표 시연 1] 자연과학 — 수평 투사 운동",
 "url":"gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/",
 "key_point":"직관: 빠르게 던지면 더 빨리 떨어질 것 같다\n변화: 수평 거리는 달라지고 낙하 시간은 같다",
 "notes":"속도를 바꾸면 멀리 가기는 합니다.\n그런데 아래로 떨어지는 시간은 같아요.\n이 앱은 수평 운동과 수직 운동의 독립성을 말보다 먼저 눈으로 보게 합니다."},

# S33
{"type":"demo","title":"[대표 시연 2] 도시 — 폭염 취약 지역",
 "url":"gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/",
 "key_point":"직관: 가장 더운 곳이 가장 먼저 지원할 곳이다\n변화: 취약 조건이 겹치면 우선 지원 지역이 바뀐다",
 "notes":"도시는 숫자 하나로 판단하기 어렵습니다.\n기온만 보면 보이는 지역과, 고령 인구나 쉼터 접근성을 함께 볼 때 보이는 지역이 달라집니다.\n사회 교과에서도 이렇게 판단 기준이 겹치는 장면을 조작 가능한 수업 장면으로 바꿀 수 있습니다."},

# S34
{"type":"demo","title":"[대표 시연 3] 법 — 계약 성립·효력 판단",
 "url":"gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/",
 "key_point":"직관: 계약서는 곧 계약의 전부다\n변화: 의사 합치, 하자, 효력 요건에 따라 판단 흐름이 달라진다",
 "notes":"법 개념은 정답 암기처럼 보이지만 실제로는 조건을 따라 판단합니다.\n조건을 바꾸면 결론이 달라지고, 어느 단계에서 판단이 갈라지는지 볼 수 있습니다."},

# S35
{"type":"content","title":"직접 요청해보세요",
 "items":[
  {"text":"먼저 3줄 스케치:","bold":True,"nobullet":True},
  {"text":"① 내 교과에서 깨고 싶은 직관"},
  {"text":"② 학생이 조작할 변수"},
  {"text":"③ 화면에서 바로 보여야 하는 변화"},
  {"text":"","nobullet":True},
  {"text":"이어서 프롬프트:","bold":True,"nobullet":True},
  {"text":'"내 교과에서 학생들이 직관적으로 오해하기 쉬운 개념 하나를 골라서, 슬라이더나 버튼으로 값을 바꾸면 결과가 바뀌는 시각화 웹앱을 HTML 파일 하나로 만들어줘. 조건: Tailwind CSS CDN / 외부 API 없음 / 직관을 스스로 발견하도록 설계"',"nobullet":True},
 ],
 "notes":"바로 만들어달라고 하기 전에, 무엇을 깨고 싶은지 먼저 정리합니다. 오늘 만든 조언자에게 이 3줄을 넣고 웹앱 아이디어를 다듬어달라고 해도 좋습니다."},

# S36
{"type":"content","title":"내 조언자 확인하기",
 "items":[
  {"text":'"지금 조언자에게 질문 하나 더 해보세요"',"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"□  프로젝트가 만들어져 있다"},
  {"text":"□  Layer 1 프로젝트 지침이 붙여넣어져 있다"},
  {"text":"□  Layer 2 파일이 업로드되어 있다"},
  {"text":"□  조언자와 대화를 나눴다"},
 ],
 "notes":"체크리스트를 확인해보세요. 하나라도 빠져 있으면 지금 채웁시다."},

# S37
{"type":"content","title":"뒤 강의에서 이 조언자로 하는 일",
 "items":[
  {"text":"뒤 6시간 강의의 출발점: 여러분의 수업 조언자","bold":True,"nobullet":True},
  {"text":"","nobullet":True},
  {"text":"Layer 2를 완성하고 수업 단원 설계에 적용"},
  {"text":"성취기준 분석, 활동 설계에 조언자 활용"},
  {"text":"수업 자료 제작에 AI 연결"},
 ],
 "notes":"뒤 강사 선생님은 여러분 조언자가 이미 있다고 전제하고 시작합니다. 오늘 만들어두신 것이 바로 뒤 강의의 시작점입니다."},

# S38
{"type":"content","title":"오늘 가져가는 것",
 "items":[
  {"text":"✓  내 수업 조언자 프로젝트 (살아있음)","nobullet":True,"bold":True},
  {"text":"✓  조언자를 써보는 방법","nobullet":True,"bold":True},
  {"text":"✓  AI로 수업 도구를 만드는 관점","nobullet":True,"bold":True},
  {"text":"","nobullet":True},
  {"text":"연수자 자료를 참고해 집에서도 이어가실 수 있습니다","nobullet":True},
 ],
 "notes":"수고 많으셨습니다. 조언자와의 대화는 오늘로 끝나지 않습니다. 수업을 준비할 때마다 꺼내 쓰시면 됩니다."},
]

# ─── Notes slide template ──────────────────────────────────────────────────────

NOTE_HEAD = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             '<p:notes xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
             'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
             'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">\n'
             '  <p:cSld>\n    <p:spTree>\n'
             '      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>\n'
             '      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
             '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>\n')
NOTE_TAIL = ('    </p:spTree>\n  </p:cSld>\n'
             '  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>\n</p:notes>')

def make_notes_xml(notes_text):
    img_ph = ('      <p:sp>\n'
              '        <p:nvSpPr><p:cNvPr id="2" name="슬라이드 이미지 1"/>'
              '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
              '<p:nvPr><p:ph type="sldImg"/></p:nvPr></p:nvSpPr>\n'
              '        <p:spPr><a:xfrm><a:off x="685800" y="685800"/>'
              '<a:ext cx="4572000" cy="3429000"/></a:xfrm></p:spPr>\n'
              '      </p:sp>\n')
    lines = notes_text.split("\n")
    paras = "".join(
        f'<a:p><a:r><a:rPr lang="ko-KR" dirty="0"/><a:t>{e(ln)}</a:t></a:r></a:p>'
        for ln in lines
    )
    body_ph = ('      <p:sp>\n'
               '        <p:nvSpPr><p:cNvPr id="3" name="노트 2"/>'
               '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
               '<p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr>\n'
               '        <p:spPr><a:xfrm><a:off x="685800" y="4343400"/>'
               '<a:ext cx="5486400" cy="3600000"/></a:xfrm></p:spPr>\n'
               f'        <p:txBody><a:bodyPr/><a:lstStyle/>{paras}</p:txBody>\n'
               '      </p:sp>\n')
    return NOTE_HEAD + img_ph + body_ph + NOTE_TAIL

# ─── Main build ────────────────────────────────────────────────────────────────

def main():
    # 1. Fresh work directory
    if WORK.exists():
        shutil.rmtree(WORK)
    shutil.copytree(TEMPLATE, WORK)

    slides_dir  = WORK / "ppt" / "slides"
    rels_dir    = slides_dir / "_rels"
    notes_dir   = WORK / "ppt" / "notesSlides"
    notes_rels  = notes_dir / "_rels"
    pres_xml    = WORK / "ppt" / "presentation.xml"
    pres_rels   = WORK / "ppt" / "_rels" / "presentation.xml.rels"
    ct_xml      = WORK / "[Content_Types].xml"

    notes_dir.mkdir(exist_ok=True)
    notes_rels.mkdir(exist_ok=True)

    # 2. Remove existing 9 slides from sldIdLst + rels + files
    pres_content = pres_xml.read_text("utf-8")
    # Collect existing slide rIds
    old_slide_rids = re.findall(r'<p:sldId[^>]+r:id="(rId\d+)"', pres_content)
    # Clear sldIdLst
    pres_content = re.sub(r'<p:sldIdLst>.*?</p:sldIdLst>', '<p:sldIdLst/>', pres_content, flags=re.DOTALL)
    pres_xml.write_text(pres_content, "utf-8")

    pres_rels_content = pres_rels.read_text("utf-8")
    for rid in old_slide_rids:
        pres_rels_content = re.sub(
            rf'\s*<Relationship[^>]*Id="{rid}"[^>]*/>\s*', '\n  ',
            pres_rels_content
        )
    pres_rels.write_text(pres_rels_content, "utf-8")

    for f in slides_dir.glob("slide*.xml"):
        f.unlink(missing_ok=True)
    for f in rels_dir.glob("slide*.xml.rels"):
        f.unlink(missing_ok=True)

    # 3. Remove existing slides from Content_Types
    ct = ct_xml.read_text("utf-8")
    ct = re.sub(r'\s*<Override PartName="/ppt/slides/[^"]*"[^/]*/>', '', ct)
    ct_xml.write_text(ct, "utf-8")

    # 4. Create 38 new slides
    new_slide_ids = []
    note_num = 1

    pres_content = pres_xml.read_text("utf-8")
    pres_rels_content = pres_rels.read_text("utf-8")
    ct = ct_xml.read_text("utf-8")

    for snum, sdata in enumerate(SLIDES, start=1):
        gen_fn, layout_file = GENERATORS[sdata["type"]]
        slide_xml = gen_fn(sdata)
        notes_text = sdata.get("notes", "")

        sfile = f"slide{snum}.xml"
        rfile = f"slide{snum}.xml.rels"

        # Write slide
        (slides_dir / sfile).write_text(slide_xml, "utf-8")

        # Write notes slide
        notes_xml = make_notes_xml(notes_text)
        nfile = f"notesSlide{note_num}.xml"
        (notes_dir / nfile).write_text(notes_xml, "utf-8")

        # Slide rels: layout + notes
        rels_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n'
                    f'  <Relationship Id="rId1" '
                    f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" '
                    f'Target="../slideLayouts/{layout_file}"/>\n'
                    f'  <Relationship Id="rId2" '
                    f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide" '
                    f'Target="../notesSlides/{nfile}"/>\n'
                    '</Relationships>')
        (rels_dir / rfile).write_text(rels_xml, "utf-8")

        # Notes rels: reference notesMaster
        notes_rels_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                          '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n'
                          '  <Relationship Id="rId1" '
                          'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster" '
                          'Target="../notesMasters/notesMaster1.xml"/>\n'
                          f'  <Relationship Id="rId2" '
                          'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" '
                          f'Target="../slides/{sfile}"/>\n'
                          '</Relationships>')
        (notes_rels / f"{nfile}.rels").write_text(notes_rels_xml, "utf-8")

        # Add to presentation rels
        rids_so_far = [int(m) for m in re.findall(r'Id="rId(\d+)"', pres_rels_content)]
        next_rid_n = max(rids_so_far) + 1 if rids_so_far else 1
        rid = f"rId{next_rid_n}"
        pres_rels_content = pres_rels_content.replace(
            '</Relationships>',
            f'  <Relationship Id="{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" '
            f'Target="slides/{sfile}"/>\n</Relationships>'
        )

        # Add to sldIdLst
        existing_ids = [int(m) for m in re.findall(r'<p:sldId[^>]+id="(\d+)"', pres_content)]
        next_id = max(existing_ids) + 1 if existing_ids else 256
        pres_content = pres_content.replace(
            '<p:sldIdLst/>',
            f'<p:sldIdLst><p:sldId id="{next_id}" r:id="{rid}"/></p:sldIdLst>'
        )
        pres_content = pres_content.replace(
            f'</p:sldIdLst>',
            f'<p:sldId id="{next_id}" r:id="{rid}"/></p:sldIdLst>'
        ) if f'<p:sldId id="{next_id}"' not in pres_content else pres_content

        new_slide_ids.append((rid, next_id, sfile))

        # Content-Types
        ct = ct.replace(
            '</Types>',
            f'  <Override PartName="/ppt/slides/{sfile}" '
            f'ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>\n'
            f'  <Override PartName="/ppt/notesSlides/{nfile}" '
            f'ContentType="application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"/>\n'
            f'</Types>'
        )

        note_num += 1

    # Write updated files
    pres_xml.write_text(pres_content, "utf-8")
    pres_rels.write_text(pres_rels_content, "utf-8")
    ct_xml.write_text(ct, "utf-8")

    print(f"Created {len(SLIDES)} slides + {len(SLIDES)} notes slides")

    # 5. Clean + Pack
    import subprocess, os
    pack_script = SKILLS / "scripts" / "office" / "pack.py"
    template_orig = Path(r"D:\Projects\AI-teacher-training\source\AI와 대화하며 만드는 나만의 수업.pptx")

    clean_script = SKILLS / "scripts" / "clean.py"
    subprocess.run(["python", str(clean_script), str(WORK)], check=True)

    result = subprocess.run(
        ["python", str(pack_script), str(WORK), str(OUTPUT),
         "--original", str(template_orig)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("PACK STDERR:", result.stderr)
        print("PACK STDOUT:", result.stdout)
        sys.exit(1)
    print(f"Packed → {OUTPUT}")

if __name__ == "__main__":
    main()
