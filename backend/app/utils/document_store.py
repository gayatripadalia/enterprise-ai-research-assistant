from app.utils.database import get_connection

def save_document(filename, text, summary):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO documents
    (filename, extracted_text, ai_summary)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (filename, text, summary))
    conn.commit()

    cursor.close()
    conn.close()