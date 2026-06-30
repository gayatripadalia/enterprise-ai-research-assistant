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

from app.utils.database import get_connection



def get_latest_document():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT extracted_text
    FROM documents
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]

    return None
def get_all_documents():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT id, filename, uploaded_at
    FROM documents
    ORDER BY uploaded_at DESC
    """

    cursor.execute(query)

    documents = cursor.fetchall()

    cursor.close()
    conn.close()

    return documents


def get_document_by_id(document_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM documents
    WHERE id = %s
    """

    cursor.execute(query, (document_id,))

    document = cursor.fetchone()

    cursor.close()
    conn.close()

    return document