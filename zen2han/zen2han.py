import sublime, sublime_plugin, zenhan

class Zen2hanCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            zen2han_text = zenhan.h2z(select_texts,zenhan.KANA)
            han2zen_text = zenhan.z2h(select_texts,zenhan.KANA)
            if select_texts != zen2han_text:
                self.view.replace(edit, region, zen2han_text)
            elif select_texts != han2zen_text:
                self.view.replace(edit, region, han2zen_text)