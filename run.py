from googletrans import Translator
import polib
import sys
	
translator = Translator()
po = polib.pofile('/home/acneidert/Documentos/workspace/incubator-superset/superset/translations/pt_BR/LC_MESSAGES/pt_BR_clean.pot')
for entry in  po.untranslated_entries():
    try:
        translation = 	translator.translate(entry.msgid, dest='pt')
        entry.msgstr = translation.text
        print entry.msgid, ' | ', translation.text, ' | ', entry.msgstr
    except:
    	print "Unexpected error:", sys.exc_info()[0]

print po.percent_translated()
po.save('/home/acneidert/Documentos/workspace/incubator-superset/superset/translations/pt_BR/LC_MESSAGES/pt_BR.po')
po.save_as_mofile('/home/acneidert/Documentos/workspace/incubator-superset/superset/translations/pt_BR/LC_MESSAGES/pt_BR.mo')