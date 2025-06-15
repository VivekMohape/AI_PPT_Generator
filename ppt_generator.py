from pptx import Presentation
from pptx.util import Pt
from schemas import SlideContent
from config import Config
from analyzer import analyze_slide_content

def generate_final_ppt_with_analysis(slide_content: SlideContent, output_path=Config.OUTPUT_PATH):
    template = Presentation(Config.TEMPLATE_PATH)
    prs_out = Presentation()
    template_slide = template.slides[0]

    slide_layout = template_slide.slide_layout
    new_slide = prs_out.slides.add_slide(slide_layout)
    for shape in template_slide.shapes:
        el = shape.element
        new_slide.shapes._spTree.insert_element_before(el, 'p:extLst')

    for shape in new_slide.shapes:
        if not shape.has_text_frame:
            continue

        placeholder_name = shape.name.lower()
        if placeholder_name == "title":
            shape.text = slide_content.title
        elif placeholder_name in slide_content.content:
            content_text = slide_content.content[placeholder_name]
            shape.text = content_text

            recommendation = analyze_slide_content(content_text, shape.width, shape.height)
            if recommendation.shrink_font and recommendation.new_font_size:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(recommendation.new_font_size)

    prs_out.save(output_path)
