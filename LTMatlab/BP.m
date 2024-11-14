function [ H_in,code_in ] = BP( H_in,code_in,degree_1_pos)        
    row = size(H_in,1);
    col = size(H_in,2);

    col_index_of_new_H = find(H_in(degree_1_pos,:) == 1);
    

    temp_H = H_in(col_index_of_new_H,:);
    H_in(col_index_of_new_H,:) = H_in(degree_1_pos,:);
    H_in(degree_1_pos,:) = temp_H;
    temp_code = code_in(col_index_of_new_H,:);
    code_in(col_index_of_new_H,:) = code_in(degree_1_pos,:);
    code_in(degree_1_pos,:) = temp_code;
    

    for i = 1:row
        if H_in(i,col_index_of_new_H) == 1 && i ~= col_index_of_new_H
            H_in(i,col_index_of_new_H) = 0;
            code_in(i,:) = rem(code_in(i,:) + code_in(col_index_of_new_H,:),2);

            degree_pos = find(H_in(i,:) == 1);
            if size(degree_pos,2) == 1
                [H_in,code_in] = BP(H_in,code_in,i);
            end
        end
    end
    

end

