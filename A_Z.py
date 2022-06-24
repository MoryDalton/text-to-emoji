def text_to_emoji(text, elm):
    all_words = {
        'A': [f'      {elm}      ', f'     {elm} {elm}     ', f'    {elm}   {elm}    ', f'   {elm} {elm} {elm} {elm}   ', f'  {elm}       {elm}  ', f' {elm}         {elm} ', f'{elm}           {elm}'],
        'B': [f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}   '],
        'C': [f'   {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'   {elm}  {elm}  {elm}  {elm}'],
        'D': [f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}   '],
        'E': [f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}  {elm}  {elm}  {elm}  {elm}'],
        'F': [f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}            '],
        'G': [f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'{elm}     {elm}  {elm}  {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}  {elm}'],
        'H': [f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}  {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}'],
        'I': [f'   {elm}  {elm}  {elm}   ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'   {elm}  {elm}  {elm}   '],
        'J': [f'   {elm}  {elm}  {elm}   ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'{elm}     {elm}      ', f'{elm}  {elm}  {elm}      '],
        'K': [f'{elm}           {elm}', f'{elm}        {elm}   ', f'{elm}     {elm}      ', f'{elm}  {elm}         ', f'{elm}     {elm}      ', f'{elm}        {elm}   ', f'{elm}           {elm}'],
        'L': [f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}            ', f'{elm}  {elm}  {elm}  {elm}  {elm}'],
        'M': [f'{elm}           {elm}', f'{elm} {elm}       {elm} {elm}', f'{elm}   {elm}   {elm}   {elm}', f'{elm}     {elm}     {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}'],
        'N': [f'{elm}           {elm}', f'{elm} {elm}         {elm}', f'{elm}   {elm}       {elm}', f'{elm}     {elm}     {elm}', f'{elm}       {elm}   {elm}', f'{elm}         {elm} {elm}', f'{elm}           {elm}'],
        'O': [f'   {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'   {elm}  {elm}  {elm}   '],
        'P': [f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}            ', f'{elm}            ', f'{elm}            '],
        'Q': [f'   {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}      {elm}    {elm}', f'{elm}        {elm}   ', f'   {elm}  {elm}     {elm}'],
        'R': [f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}  {elm}  {elm}  {elm}   ', f'{elm}  {elm}         ', f'{elm}      {elm}     ', f'{elm}          {elm} '],
        'S': [f'   {elm}  {elm}  {elm}  {elm}', f'{elm}            ', f'{elm}            ', f'   {elm}  {elm}  {elm}   ', f'            {elm}', f'            {elm}', f'{elm}  {elm}  {elm}  {elm}   '],
        'T': [f'{elm}  {elm}  {elm}  {elm}  {elm}', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      '],
        'U': [f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'   {elm}  {elm}  {elm}   '],
        'V': [f'{elm}           {elm}', f' {elm}         {elm} ', f'  {elm}       {elm}  ', f'   {elm}     {elm}   ', f'    {elm}   {elm}    ', f'     {elm} {elm}     ', f'      {elm}      '],
        'W': [f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}           {elm}', f'{elm}     {elm}     {elm}', f'{elm}   {elm}   {elm}   {elm}', f'{elm} {elm}       {elm} {elm}', f'{elm}           {elm}'],
        'X': [f'{elm}           {elm}', f'  {elm}       {elm}  ', f'    {elm}   {elm}    ', f'      {elm}      ', f'    {elm}   {elm}    ', f'  {elm}       {elm}  ', f'{elm}           {elm}'],
        'Y': [f'{elm}           {elm}', f'  {elm}       {elm}  ', f'    {elm}   {elm}    ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      ', f'      {elm}      '],
        'Z': [f'{elm}  {elm}  {elm}  {elm}  {elm}', f'          {elm}  ', f'        {elm}    ', f'      {elm}      ', f'    {elm}        ', f'  {elm}          ', f'{elm}  {elm}  {elm}  {elm}  {elm}']
    }

    t = list(text)
    l = []

    for i in t:

        l.append(all_words.get(i))

    return show(l)


def show(l):

    all_list = []
    for i in range(7):

        s = []

        for j in range(len(l)):

            s.append(l[j][i])

        all_list.append((5*' ').join(s))
    result = '\n'.join(all_list)
    return result

