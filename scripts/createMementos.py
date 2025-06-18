import os

cwd = os.getcwd()

content = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<memento show_menu="true" show_statusbar="true" show_tabs="false" show_toolbar="true">
    <DockStage_MAIN height="857.0" width="1920.0" x="0.0" y="32.0">
        <split pos="0.8070907194994786">
            <pane selected="0">
                <DockItem_3324f349_58a9_47f9_b3be_5b1061b6d099 application="display_runtime" input_uri="file:"""+cwd+"""/topup/main.bob" toolbar="true"/>
            </pane>
            <pane selected="0">
                <DockItem_88556356_7856_45a3_bc93_f0a2dbb855a4 application="display_runtime" input_uri="file:"""+cwd+"""/topup/topup_properties.bob" toolbar="true"/>
                <DockItem_11d3b12e_8fe6_422c_a6b2_52017d1027b4 application="display_runtime" input_uri="file:"""+cwd+"""/topup/fill_properties.bob" toolbar="true"/>
            </pane>
        </split>
    </DockStage_MAIN>
</memento>
"""


with open("mementos/topup.memento", "w") as f:
  f.write(content)